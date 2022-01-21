# PZSP2

# Instrukcja obsługi

## 1. Strona startowa

To jest strona powitalna *(rys 1.1)*. 
Można na niej przeczytać zamieszczone aktualności oraz przejść do ekranu logowania.

<div style="display:flex; flex-direction: column; justify-content:center; align-items:center">
    <img src="https://i.imgur.com/KmiutCF.png" />
    <p>Rys. 1.1 Strona powitalna </p>
</div>

## 2. Strona logowania
Możemy się zalogować na trzy rodzaje kont *(rys. 2.1)*:
* Administrator
* Doktor
* Pacjent

<div style="display:flex; flex-direction: column; justify-content:center; align-items:center">
    <img src="https://i.imgur.com/AKDdCUq.png" />
    <p>Rys. 2.1 Strona logowania </p>
</div>

## 3. Panel doktora
### 3.1 Strona główna (Profil)
Na swojej stronie domowej można: 
- zmienić swoje hasło *(rys. 3.1)*
<div style="display:flex; flex-direction: column; justify-content:center; align-items:center">
    <img src="https://i.imgur.com/QjUK5or.png" />
    <p>Rys. 3.1 Panel zmiany hasła </p>
</div>

- przejść za pomocą panelu nawigacji do podstrony lub wylogować się *(rys 3.2)*

<div style="display:flex; flex-direction: column; justify-content:center; align-items:center">
    <img src="https://i.imgur.com/ViqOlSX.png" />
    <p>Rys. 3.2 Boczny panel nawigacji doktora </p>
</div>

### 3.2 Rozpoczynanie analizy
W celu rozpoczęcia analizy, należy wybrać pacjenta którego ona dotyczy. Wybieramy w bocznym panelu nawigacji doktora zakładkę `Nowa analiza`. Pojawi  się obszar wyszukiwania pacjenta *(rys. 3.3)*. Możemy wyszukać pacjenta po którymkolwiek kryterium. Wpisane kryterium nie musi być pełne. Oznacza to, że możemy wyszukać pacjenta o imieniu "Adrian" po wpisaniu "Adri" i zainicjowaniu wyszukiwania zielonym przyciskiem `Wyszukaj` na dole obszaru wyszukiwania.

<div style="display:flex; flex-direction: column; justify-content:center; align-items:center">
    <img src="https://i.imgur.com/ml4CEpY.png" />
    <p>Rys. 3.3 Obszar wyszukiwania pacjenta </p>
</div>

Po wyszukaniu pacjenta pojawią się wszyscy pacjenci pasujący do podanego kryterium w tabelce pod obszarem wyszukiwania *(rys. 3.4)*. Jeśli w tabeli nie pojawia się poszukiwany pacjent, oznacza to, że nie mamy do niego dostępu lub nie ma go w systemie. Brak dostępu oznacza, że administrator nie przypisał danego pacjenta do doktora.

<div style="display:flex; flex-direction: column; justify-content:center; align-items:center">
    <img src="https://i.imgur.com/4E2ZWDA.png" />
    <p>Rys. 3.4 Okno wyszukiwania pacjenta wraz z tabelą znalezionych pacjentów </p>
</div>

Wybieramy pacjenta, dla którego przeprowadzamy analizę przyciskiem `Wybierz` w tabeli. Zostaniemy przekierowani na stronę przesyłania pliku dźwiękowego *(rys. 3.5)*, który zostanie poddany analizie. W tym oknie wybieramy plik poprzez kliknięcie w ikonę spinacza lub w polę `Wybierz plik`.
<div style="display:flex; flex-direction: column; justify-content:center; align-items:center">
    <img src="https://i.imgur.com/pQwa7WS.png" />
    <p>Rys. 3.5 Okno wyboru pliku przed wybraniem pliku</p>
</div>

Po wybraniu pliku przycisk `Rozpocznij analizę` zmieni kolor na zielony *(rys. 3.6)*. Możemy teraz zmienić plik, ponownie klikając w wymienione wyżej elementy, albo potwierdzić jego wybór klikając w zielony przycisk `Rozpocznij analizę`.

<div style="display:flex; flex-direction: column; justify-content:center; align-items:center">
    <img src="https://i.imgur.com/yUnLw18.png" />
    <p>Rys. 3.6 Okno wyboru pliku po wybraniu pliku </p>
</div>

Po kliknięciu przycisku `Rozpocznij analizę`, pokaże się informacja o jej uruchomieniu oraz przycisk `Wyniki analizy`, który przekierowuje do wyników analizy *(rys 3.7)*.
<div style="display:flex; flex-direction: column; justify-content:center; align-items:center">
    <img src="https://i.imgur.com/vTuXo6J.png" />
    <p>Rys. 3.7 Przycisk przekierowujący do strony wyników analizy </p>
</div>


Przetworzenie analizy zajmuje odrobinę czasu. Zależnie od długości pliku, analiza może potrwać od kilku sekund do kilku minut w przypadku bardzo długich plików. Gdy wyniki będą już dostępne. dostaniemy powiadomienie na dole ekranu *(rys 3.8)*.

<div style="display:flex; flex-direction: column; justify-content:center; align-items:center">
    <img src="https://i.imgur.com/ji5IzGi.png" />
    <p>Rys. 3.8 Powiadomienie o zakończeniu analizy </p>
</div>

Po wejściu w wyniki analizy, jeśli analiza nie została jeszcze zakończona, pojawi się animowany ekran ładowania *(rys. 3.9)*.

<div style="display:flex; flex-direction: column; justify-content:center; align-items:center">
    <img src="https://i.imgur.com/qczyvQx.png" />
    <p>Rys. 3.9 Ekran ładowania analizy </p>
</div>


W przeciwnym wypadku ukaże nam się wykres *(rys. 3.10)* oraz statystyki analizy *(rys. 3.11)*.

<div style="display:flex; flex-direction: column; justify-content:center; align-items:center">
    <img src="https://i.imgur.com/WiSsVYF.png" />
    <p>Rys. 3.10 Wykres analizy </p>
</div>

<div style="display:flex; flex-direction: column; justify-content:center; align-items:center">
    <img src="https://i.imgur.com/EL1Fm5z.png" />
    <p>Rys. 3.11 Statystyki analizy </p>
</div>

### 3.3 Sprawdzanie wyników pacjenta
Proces pobierania wyników wygląda podobnie jak w punkcie ***3.2** Rozpoczynanie analizy (Rys. 3.3-3.4)*. Wybieramy w bocznym panelu nawigacji doktora zakładkę `Dane pacjenta`. Po wyszukaniu pacjenta ukażą nam się jego dane oraz jego dotychczasowe analizy *(Rys. 3.12)*.

<div style="display:flex; flex-direction: column; justify-content:center; align-items:center">
    <img src="https://i.imgur.com/bzxi4Pp.png" />
    <p>Rys. 3.12 Dane i wyniki pacjenta </p>
</div>

Analizy mają różne statusy. 
* `PENDING` - analiza jest przeprowadzana
* `COMPLETED` - analiza została ukończona
* `CREATED` - analiza czeka w kolejce
* `FAILED` - wystąpił błąd z analizą

Z wyświetlonej listy *(rys. 3.12)* możemy wyświetlić wyniki analizy klikając w przycisk `Pokaż wyniki`. Ukażą się wykres *(rys. 3.10)* oraz statystyki analizy *(rys. 3.11)*.


### 3.4 Przeglądanie nagrań pacjenta
Proces wyszukiwania pacjenta wygląda podobnie jak w punkcie *3.2 Rozpoczynanie analizy (Rys. 3.3-3.4)*. Wybieramy w bocznym panelu nawigacji doktora zakładkę `Dane pacjenta`. Po wyszukaniu pacjenta wyświetlą się nagrania pacjenta, które były poddawane analizie *(rys. 3.13)*.

<div style="display:flex; flex-direction: column; justify-content:center; align-items:center">
    <img src="https://i.imgur.com/2ny8utj.png" />
    <p>Rys. 3.13 Historia nagrań </p>
</div>

Z poziomu listy *(rys. 3.13)* możemy pobrać pliki dźwiękowe, lub ponownie rozpocząć analizę dla wybranego pliku. Akcje wykonają się po kliknięciu przycisku w kolumnie `pobierz`/`ponowna analiza`.


## 4. Panel Pacjenta
### 4.1 Strona główna (Profil)
Jako pacjent, na stronie domowej można: 
- zmienić swoje hasło *(rys. 4.1)*.
<div style="display:flex; flex-direction: column; justify-content:center; align-items:center">
    <img src="https://i.imgur.com/QjUK5or.png" />
    <p>Rys. 4.1 Panel zmiany hasła </p>
</div>

- przejść za pomocą panelu nawigacji do innej podstrony lub wylogować się *(rys 4.2)*.

<div style="display:flex; flex-direction: column; justify-content:center; align-items:center">
    <img src="https://i.imgur.com/H5ZcaCq.png" />
    <p>Rys. 4.2 Boczny panel nawigacji pacjenta </p>
</div>

### 4.2 Przeglądanie własnych analiz
Klikamy w zakładkę bocznego panelu nawigacji o nazwie `Moje analizy`. Zostajemy przeniesieni do strony z naszymi danymi i analizami *(rys. 4.3)*.

<div style="display:flex; flex-direction: column; justify-content:center; align-items:center">
    <img src="https://i.imgur.com/S6B7uQk.png" />
    <p>Rys. 4.3 Dane osobowe i tabela analiz pacjenta </p>
</div>

Możemy tutaj wybrać analizę, której wyniki chcemy przejrzeć. Klikamy w tym celu w przycisk `Pokaż wyniki`. Po wejściu w wyniki analizy, jeśli analiza nie została jeszcze zakończona, pojawi się animowany ekran ładowania *(rys. 3.9)*.

<div style="display:flex; flex-direction: column; justify-content:center; align-items:center">
    <img src="https://i.imgur.com/qczyvQx.png" />
    <p>Rys. 4.4 Ekran ładowania analizy </p>
</div>


W przeciwnym wypadku ukaże nam się wykres *(rys. 4.5)* oraz statystyki analizy *(rys. 4.6)*.

<div style="display:flex; flex-direction: column; justify-content:center; align-items:center">
    <img src="https://i.imgur.com/WoUkAud.png" />
    <p>Rys. 4.5 Wykres analizy </p>
</div>

<div style="display:flex; flex-direction: column; justify-content:center; align-items:center">
    <img src="https://i.imgur.com/EL1Fm5z.png" />
    <p>Rys. 4.6 Statystyki analizy </p>
</div>
