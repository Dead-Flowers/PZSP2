from os import stat
from pydoc import cli, doc
from typing import Dict
from unittest.mock import patch

from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from uuid import uuid4
from app import crud
from app.core.config import settings
from app.schemas.recording import RecordingCreate
from app.schemas.user import UserCreate, UserUpdate
from app.schemas.analysis_result import (
    AnalysisResultCreate,
)
from app.tests.utils.utils import (
    random_email,
    random_lower_string,
    random_pesel,
    random_bytes,
)
from app.tests.utils.user import (
    create_random_patient,
    create_random_user,
    user_authentication_headers,
)


def test_get_existing_recording(
    client: TestClient, normal_user_token_headers: Dict[str, str], db: Session
) -> None:

    patient, _, _ = create_random_patient(db)
    doctor, email, password = create_random_user(db)
    doctor_header = user_authentication_headers(
        client=client, email=email, password=password
    )
    doctor_id = doctor.id
    patient_id = patient.id
    patient = crud.user.update(
        db, db_obj=patient, obj_in=UserUpdate(doctor_id=doctor_id)
    )

    rec_in = RecordingCreate(
        blob=random_bytes(256), filename=random_lower_string(), patient_id=patient_id
    )
    recording = crud.recording.create(db, obj_in=rec_in)
    recording_id = recording.id
    r = client.get(
        f"{settings.API_V1_STR}/analysis/recordings/{recording_id}",
        headers=doctor_header,
    )

    assert 200 <= r.status_code < 300
    recording_returned = r.json()
    assert recording_returned["filename"] == recording.filename
    assert recording_returned["patient_id"] == str(recording.patient_id)
    assert recording_returned["byte_length"] == recording.byte_length


def test_get_existing_recordings_with_patient_id(
    client: TestClient, normal_user_token_headers: Dict[str, str], db: Session
) -> None:

    patient, _, _ = create_random_patient(db)
    doctor, email, password = create_random_user(db)
    doctor_header = user_authentication_headers(
        client=client, email=email, password=password
    )
    doctor_id = doctor.id
    patient_id = patient.id
    patient = crud.user.update(
        db, db_obj=patient, obj_in=UserUpdate(doctor_id=doctor_id)
    )

    rec_in = RecordingCreate(
        blob=random_bytes(256), filename=random_lower_string(), patient_id=patient_id
    )
    recording = crud.recording.create(db, obj_in=rec_in)
    recording_id = recording.id
    r = client.get(
        f"{settings.API_V1_STR}/analysis/recordings",
        headers=doctor_header,
        params=dict(patient_id=patient_id),
    )

    recordings = r.json()
    assert 200 <= r.status_code < 300
    assert len(recordings) == 1


def test_get_existing_recordings_as_admin(
    client: TestClient, superuser_token_headers: Dict[str, str], db: Session
) -> None:

    patient, _, _ = create_random_patient(db)
    doctor, email, password = create_random_user(db)
    doctor_header = user_authentication_headers(
        client=client, email=email, password=password
    )
    doctor_id = doctor.id
    patient_id = patient.id
    patient = crud.user.update(
        db, db_obj=patient, obj_in=UserUpdate(doctor_id=doctor_id)
    )
    previous_recs_count = crud.recording.get_multi(db)

    rec_in = RecordingCreate(
        blob=random_bytes(256), filename=random_lower_string(), patient_id=patient_id
    )
    recording = crud.recording.create(db, obj_in=rec_in)

    recording_id = recording.id
    r = client.get(
        f"{settings.API_V1_STR}/analysis/recordings",
        headers=superuser_token_headers,
    )

    recordings = r.json()
    assert 200 <= r.status_code < 300


def test_download_existing_recording_with_patient_id(
    client: TestClient, normal_user_token_headers: Dict[str, str], db: Session
) -> None:

    patient, _, _ = create_random_patient(db)
    doctor, email, password = create_random_user(db)
    doctor_header = user_authentication_headers(
        client=client, email=email, password=password
    )
    doctor_id = doctor.id
    patient_id = patient.id
    patient = crud.user.update(
        db, db_obj=patient, obj_in=UserUpdate(doctor_id=doctor_id)
    )

    rec_in = RecordingCreate(
        blob=random_bytes(256), filename=random_lower_string(), patient_id=patient_id
    )
    recording = crud.recording.create(db, obj_in=rec_in)
    recording_id = recording.id
    r = client.post(
        f"{settings.API_V1_STR}/analysis/recordings/{recording_id}/download",
        headers=doctor_header,
    )

    assert 200 <= r.status_code < 300


def test_perform_analysis(
    client: TestClient,
    normal_user_token_headers: Dict[str, str],
    db: Session,
) -> None:

    patient, _, _ = create_random_patient(db)
    doctor, email, password = create_random_user(db)
    doctor_header = user_authentication_headers(
        client=client, email=email, password=password
    )
    doctor_id = doctor.id
    patient_id = patient.id
    patient = crud.user.update(
        db, db_obj=patient, obj_in=UserUpdate(doctor_id=doctor_id)
    )

    rec_in = RecordingCreate(
        blob=random_bytes(256), filename=random_lower_string(), patient_id=patient_id
    )
    recording = crud.recording.create(db, obj_in=rec_in)
    recording_id = recording.id

    with patch("app.worker.app.send_file.delay") as mock_task:
        r = client.post(
            f"{settings.API_V1_STR}/analysis/recordings/{recording_id}/analyze",
            headers=doctor_header,
        )
        assert 200 <= r.status_code < 300
        assert mock_task.called == True
        analysis = crud.analysis_result.get(db, r.json())
        assert analysis.recording_id == recording_id


def test_get_analysis(
    client: TestClient,
    normal_user_token_headers: Dict[str, str],
    db: Session,
) -> None:

    patient, _, _ = create_random_patient(db)
    doctor, email, password = create_random_user(db)
    doctor_header = user_authentication_headers(
        client=client, email=email, password=password
    )
    doctor_id = doctor.id
    patient_id = patient.id
    patient = crud.user.update(
        db, db_obj=patient, obj_in=UserUpdate(doctor_id=doctor_id)
    )

    rec_in = RecordingCreate(
        blob=random_bytes(256), filename=random_lower_string(), patient_id=patient_id
    )
    recording = crud.recording.create(db, obj_in=rec_in)
    recording_id = recording.id

    an_in = AnalysisResultCreate(
        status="CREATED", patient_id=patient_id, recording_id=recording_id
    )
    analysis = crud.analysis_result.create(db, obj_in=an_in)
    analysis_id = analysis.id

    r = client.get(
        f"{settings.API_V1_STR}/analysis/results/{analysis_id}",
        headers=doctor_header,
    )
    data = r.json()
    assert 200 <= r.status_code < 300
    assert data["recording_id"] == str(recording_id)
    assert data["id"] == str(analysis_id)
    assert data["status"] == "CREATED"
    assert data["patient_id"] == str(patient_id)


def test_get_analysis_as_patient(
    client: TestClient,
    normal_user_token_headers: Dict[str, str],
    db: Session,
) -> None:

    patient, p_email, p_password = create_random_patient(db)
    patient_header = user_authentication_headers(
        client=client, email=p_email, password=p_password
    )
    doctor, email, password = create_random_user(db)
    doctor_header = user_authentication_headers(
        client=client, email=email, password=password
    )
    doctor_id = doctor.id
    patient_id = patient.id
    patient = crud.user.update(
        db, db_obj=patient, obj_in=UserUpdate(doctor_id=doctor_id)
    )

    rec_in = RecordingCreate(
        blob=random_bytes(256), filename=random_lower_string(), patient_id=patient_id
    )
    recording = crud.recording.create(db, obj_in=rec_in)
    recording_id = recording.id

    an_in = AnalysisResultCreate(
        status="CREATED", patient_id=patient_id, recording_id=recording_id
    )
    analysis = crud.analysis_result.create(db, obj_in=an_in)
    analysis_id = analysis.id

    r = client.get(
        f"{settings.API_V1_STR}/analysis/results/{analysis_id}",
        headers=patient_header,
    )
    data = r.json()
    assert 200 <= r.status_code < 300
    assert data["recording_id"] == str(recording_id)
    assert data["id"] == str(analysis_id)
    assert data["status"] == "CREATED"
    assert data["patient_id"] == str(patient_id)


def test_get_analysis_stats(
    client: TestClient,
    superuser_token_headers: Dict[str, str],
    db: Session,
) -> None:

    patient, _, _ = create_random_patient(db)
    doctor, email, password = create_random_user(db)
    doctor_header = user_authentication_headers(
        client=client, email=email, password=password
    )
    doctor_id = doctor.id
    patient_id = patient.id
    patient = crud.user.update(
        db, db_obj=patient, obj_in=UserUpdate(doctor_id=doctor_id)
    )

    rec_in = RecordingCreate(
        blob=random_bytes(256), filename=random_lower_string(), patient_id=patient_id
    )
    recording = crud.recording.create(db, obj_in=rec_in)
    recording_id = recording.id

    an_in = AnalysisResultCreate(
        status="COMPLETED", patient_id=patient_id, recording_id=recording_id
    )
    analysis = crud.analysis_result.create(db, obj_in=an_in)
    analysis_id = analysis.id

    an_in = AnalysisResultCreate(
        status="FAILED", patient_id=patient_id, recording_id=recording_id
    )
    analysis = crud.analysis_result.create(db, obj_in=an_in)
    analysis_id = analysis.id

    r = client.get(
        f"{settings.API_V1_STR}/analysis/stats",
        headers=superuser_token_headers,
    )
    data = r.json()
    assert 200 <= r.status_code < 300
    assert int(data["success"]) >= 1
    assert int(data["failure"]) >= 1


def test_get_analysis_stats_as_doctor_forbidden(
    client: TestClient,
    superuser_token_headers: Dict[str, str],
    db: Session,
) -> None:

    patient, _, _ = create_random_patient(db)
    doctor, email, password = create_random_user(db)
    doctor_header = user_authentication_headers(
        client=client, email=email, password=password
    )
    doctor_id = doctor.id
    patient_id = patient.id
    patient = crud.user.update(
        db, db_obj=patient, obj_in=UserUpdate(doctor_id=doctor_id)
    )

    rec_in = RecordingCreate(
        blob=random_bytes(256), filename=random_lower_string(), patient_id=patient_id
    )
    recording = crud.recording.create(db, obj_in=rec_in)
    recording_id = recording.id

    an_in = AnalysisResultCreate(
        status="COMPLETED", patient_id=patient_id, recording_id=recording_id
    )
    analysis = crud.analysis_result.create(db, obj_in=an_in)
    analysis_id = analysis.id

    an_in = AnalysisResultCreate(
        status="FAILED", patient_id=patient_id, recording_id=recording_id
    )
    analysis = crud.analysis_result.create(db, obj_in=an_in)
    analysis_id = analysis.id

    r = client.get(
        f"{settings.API_V1_STR}/analysis/stats",
        headers=doctor_header,
    )
    assert r.status_code == 403


def test_get_analysis_status(
    client: TestClient,
    normal_user_token_headers: Dict[str, str],
    db: Session,
) -> None:

    patient, _, _ = create_random_patient(db)
    doctor, email, password = create_random_user(db)
    doctor_header = user_authentication_headers(
        client=client, email=email, password=password
    )
    doctor_id = doctor.id
    patient_id = patient.id
    patient = crud.user.update(
        db, db_obj=patient, obj_in=UserUpdate(doctor_id=doctor_id)
    )

    rec_in = RecordingCreate(
        blob=random_bytes(256), filename=random_lower_string(), patient_id=patient_id
    )
    recording = crud.recording.create(db, obj_in=rec_in)
    recording_id = recording.id

    an_in = AnalysisResultCreate(
        status="CREATED", patient_id=patient_id, recording_id=recording_id
    )
    analysis = crud.analysis_result.create(db, obj_in=an_in)
    analysis_id = analysis.id

    r = client.get(
        f"{settings.API_V1_STR}/analysis/results/{analysis_id}/status",
        headers=doctor_header,
    )
    data = r.json()
    assert 200 <= r.status_code < 300
    assert data == "CREATED"


def test_get_results_as_doctor(
    client: TestClient,
    superuser_token_headers: Dict[str, str],
    db: Session,
) -> None:

    patient, _, _ = create_random_patient(db)
    doctor, email, password = create_random_user(db)
    doctor_header = user_authentication_headers(
        client=client, email=email, password=password
    )
    doctor_id = doctor.id
    patient_id = patient.id
    patient = crud.user.update(
        db, db_obj=patient, obj_in=UserUpdate(doctor_id=doctor_id)
    )

    rec_in = RecordingCreate(
        blob=random_bytes(256), filename=random_lower_string(), patient_id=patient_id
    )
    recording = crud.recording.create(db, obj_in=rec_in)
    recording_id = recording.id

    an_in = AnalysisResultCreate(
        status="COMPLETED", patient_id=patient_id, recording_id=recording_id
    )
    analysis = crud.analysis_result.create(db, obj_in=an_in)
    analysis_id = analysis.id

    an_in = AnalysisResultCreate(
        status="FAILED", patient_id=patient_id, recording_id=recording_id
    )
    analysis = crud.analysis_result.create(db, obj_in=an_in)
    analysis_id = analysis.id

    r = client.get(
        f"{settings.API_V1_STR}/analysis/results",
        headers=doctor_header,
    )
    data = r.json()
    assert 200 <= r.status_code < 300
    assert len(data) >= 2


def test_get_results_as_doctor_with_patient_id(
    client: TestClient,
    superuser_token_headers: Dict[str, str],
    db: Session,
) -> None:

    patient, _, _ = create_random_patient(db)
    doctor, email, password = create_random_user(db)
    doctor_header = user_authentication_headers(
        client=client, email=email, password=password
    )
    doctor_id = doctor.id
    patient_id = patient.id
    patient = crud.user.update(
        db, db_obj=patient, obj_in=UserUpdate(doctor_id=doctor_id)
    )

    rec_in = RecordingCreate(
        blob=random_bytes(256), filename=random_lower_string(), patient_id=patient_id
    )
    recording = crud.recording.create(db, obj_in=rec_in)
    recording_id = recording.id

    an_in = AnalysisResultCreate(
        status="COMPLETED", patient_id=patient_id, recording_id=recording_id
    )
    analysis = crud.analysis_result.create(db, obj_in=an_in)
    analysis_id = analysis.id

    an_in = AnalysisResultCreate(
        status="FAILED", patient_id=patient_id, recording_id=recording_id
    )
    analysis = crud.analysis_result.create(db, obj_in=an_in)
    analysis_id = analysis.id

    r = client.get(
        f"{settings.API_V1_STR}/analysis/results",
        headers=doctor_header,
        params=dict(patient_id=patient_id),
    )
    data = r.json()
    assert 200 <= r.status_code < 300
    assert len(data) == 2


def test_get_results_as_admin(
    client: TestClient,
    superuser_token_headers: Dict[str, str],
    db: Session,
) -> None:

    patient, _, _ = create_random_patient(db)
    doctor, email, password = create_random_user(db)
    doctor_header = user_authentication_headers(
        client=client, email=email, password=password
    )
    doctor_id = doctor.id
    patient_id = patient.id
    patient = crud.user.update(
        db, db_obj=patient, obj_in=UserUpdate(doctor_id=doctor_id)
    )

    rec_in = RecordingCreate(
        blob=random_bytes(256), filename=random_lower_string(), patient_id=patient_id
    )
    recording = crud.recording.create(db, obj_in=rec_in)
    recording_id = recording.id

    an_in = AnalysisResultCreate(
        status="COMPLETED", patient_id=patient_id, recording_id=recording_id
    )
    analysis = crud.analysis_result.create(db, obj_in=an_in)
    analysis_id = analysis.id

    an_in = AnalysisResultCreate(
        status="FAILED", patient_id=patient_id, recording_id=recording_id
    )
    analysis = crud.analysis_result.create(db, obj_in=an_in)
    analysis_id = analysis.id

    r = client.get(
        f"{settings.API_V1_STR}/analysis/results",
        headers=superuser_token_headers,
    )
    data = r.json()
    assert 200 <= r.status_code < 300
    assert len(data) >= 2


def test_get_results_as_patient(
    client: TestClient,
    superuser_token_headers: Dict[str, str],
    db: Session,
) -> None:

    patient, p_email, p_password = create_random_patient(db)
    patient2, _, _ = create_random_patient(db)
    patient_header = user_authentication_headers(
        client=client, email=p_email, password=p_password
    )
    doctor, email, password = create_random_user(db)
    doctor_header = user_authentication_headers(
        client=client, email=email, password=password
    )
    doctor_id = doctor.id
    patient_id = patient.id
    patient2_id = patient2.id
    patient = crud.user.update(
        db, db_obj=patient, obj_in=UserUpdate(doctor_id=doctor_id)
    )
    patient2 = crud.user.update(
        db, db_obj=patient2, obj_in=UserUpdate(doctor_id=doctor_id)
    )

    rec_in = RecordingCreate(
        blob=random_bytes(256), filename=random_lower_string(), patient_id=patient_id
    )
    recording = crud.recording.create(db, obj_in=rec_in)
    recording_id = recording.id

    rec_in = RecordingCreate(
        blob=random_bytes(256), filename=random_lower_string(), patient_id=patient2_id
    )
    recording = crud.recording.create(db, obj_in=rec_in)
    recording2_id = recording.id

    an_in = AnalysisResultCreate(
        status="COMPLETED", patient_id=patient_id, recording_id=recording_id
    )
    analysis = crud.analysis_result.create(db, obj_in=an_in)
    analysis_id = analysis.id

    an_in = AnalysisResultCreate(
        status="FAILED", patient_id=patient2_id, recording_id=recording2_id
    )
    analysis = crud.analysis_result.create(db, obj_in=an_in)
    analysis2_id = analysis.id

    r = client.get(
        f"{settings.API_V1_STR}/analysis/results",
        headers=patient_header,
    )
    data = r.json()
    assert 200 <= r.status_code < 300
    assert len(data) == 1
