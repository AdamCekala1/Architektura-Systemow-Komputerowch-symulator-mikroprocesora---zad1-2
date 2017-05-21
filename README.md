#

Program główny : askgui.py

#


Zadanie 1.

Wykorzystując dowolny język programowania dla komputerów w standardzie PC napisać aplikację stanowiącą model

programowego symulatora mikroprocesora. Program powinien mieć przyjazny interfejs użytkownika graficzny lub znakowy do

uznania przez autorów. Należy przyjąć następujący model naszego procesora:

• Procesor posiada cztery 16-bitowe rejestry ogólnego przeznaczenia oznaczone jako AX, BX, CX i DX;

• Każdy z rejestrów powinien być traktowany jako para 8-bitowych rejestrów o oznaczeniach NH dla części starszej i NL

dla części młodszej gdzie N oznacza A albo B albo C albo D;

• Lista rozkazów naszego procesora obejmuje trzy rozkazy MOV – przesłania, ADD – dodawania i SUB – odejmowania;

• Procesor umożliwia realizację dwóch trybów adresowania: trybu rejestrowego oraz trybu natychmiastowego;

• Program umożliwia pisanie krótkich programów z użyciem dostępnych rozkazów i trybów adresowania;

• Program umożliwia realizację napisanych programów w trybie całościowego wykonania i w trybie pracy krokowej.

• W trybie pracy krokowej należy zapewnić śledzenie kolejności wykonywanych instrukcji. Zalecenie to należy

zrealizować stosując numeracje linii kodu programu oraz odwołania do numeru aktualnie wykonywanej instrukcji.

• Program symulatora umożliwia zapisanie do pliku a następnie ponowne wczytanie napisanego wcześniej programu w

celu jego dalszej edycji i ponownego uruchomienia.

Opracowanemu programowi powinna towarzyszyć dokumentacja – sprawozdanie. Sprawozdanie powinno zawierać:

• Sformułowanie zadania wraz z przyjęciem założeń szczegółowych np. w zakresie stosowanej składni, separatorów kodów

mnemotechnicznych i argumentów itd.;

• Opis przyjętych rozwiązań programowych zilustrowanych ewentualnie fragmentami kodu (nie zamieszczać wydruków całych

programów!) dotyczących kluczowych kwestii programu np. parsing linii programu;

• Dyskusję osiągniętych wyników z wskazaniem wad i zalet napisanej aplikacji.

Termin zaliczania 6-7 tydzień

Zadanie 2.

Rozszerzyć możliwości modelu programowego symulatora mikroprocesora opracowanego w zadaniu 1 tak aby umożliwiał

on symulację realizacji dziesięciu funkcji przerwań procesora oferowanych przez moduł BIOS (można też użyć przerwań DOS).

Wybrane funkcje powinny być różnorodne, dotyczyć różnych zasobów komputera PC np. zegara RTC, klawiatury, monitora

ekranowego, pamięci dyskowej. Aplikacja powinna realizować dwa wątki:

• dydaktyczny – prezentujący w wyczerpujący sposób opis działania funkcji oraz sposób jej programowego

wykorzystania obejmujący sposób wywoływania oraz przekazywania parametrów oraz wyjaśniający znaczenie tych

parametrów.

• demonstracyjny – prezentujący wybrane funkcje w działaniu.

W celu realizacji wątku demonstracyjnego do zbioru nazw dotychczas realizowanych komend (MOV, ADD, SUB) należy dodać

INTxx, INTyy, INTzz, ..... , gdzie xx, yy, zz, .... oznaczają numery wybranych przerwań. W programie należy utworzyć STOS

służący do przechowywania zawartości rejestrów procesora na czas wykonywania przerwań. (Szczegółowy opis mechanizmu

wywoływania przerwań procesora zostanie podany przez prowadzącego w odrębnym załączniku.)

Opracowanemu programowi powinna towarzyszyć dokumentacja – sprawozdanie. Sprawozdanie powinno zawierać:

 sformułowanie zadania wraz z przyjęciem założeń szczegółowych np. opisu wybranych funkcji i sposobu ich wykorzystania

itd.;

 opis przyjętych rozwiązań programowych zilustrowanych ewentualnie fragmentami kodu (nie zamieszczać wydruków całych

programów!);

 dyskusję osiągniętych wyników z wskazaniem wad i zalet napisanej aplikacji.
