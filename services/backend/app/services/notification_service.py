from typing import List, Tuple
from sqlalchemy.orm import Session
from app.models.result import AnalysisResult
from app.models.ws_messages import AnalysisStateUpdated
from app.crud import analysis_result
from app.crud import user


class NotificationService:
    def get_analysis_update_recipients(
        self, db: Session, analysis_id: str
    ) -> List[str]:
        recipients = []
        # notify the patient
        analysis = analysis_result.get(db, analysis_id)
        recipients.append(analysis.patient_id)
        # notify the patient's doctor
        patient = user.get(db, analysis.patient_id)
        if patient.doctor_id:
            recipients.append(patient.doctor_id)

        return recipients


notificationService = NotificationService()
