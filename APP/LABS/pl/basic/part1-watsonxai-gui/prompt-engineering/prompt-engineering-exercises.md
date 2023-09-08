# Prompt engineering ćwiczenia

Wykonaj poniższe ćwiczenia wykorzystując Prompt Lab z watsonx.ai.

**Ćwiczenia**
<table>
<tr>
<td><a href="#1-classify">1. Klasyfikacja</a></td>
<td>Wykrywaj intencje użytkowników chatbota</td>
</tr>
<tr>
<td><a href="#2-rewrite">2. Przekształcenia programistyczne</a></td>
<td>Przekształć Markdown do HTML</td>
</tr>
<tr>
<td><a href="#3-study-questions">3. Przewidywanie pytań</a></td>
<td>Przewiduj potencjalne pytania klientów</td>
</tr>
<tr>
<td><a href="#4-text-extraction">4. Ekstrakcja tekstu</a></td>
<td>Wyodrębnij imiona ze zdania</td>
</tr>
<tr>
<td><a href="#5-summarization">5. Sumaryzacja</a></td>
<td>Streść podany tekst</td>
</tr>
</table>

<p>&nbsp;</p>


## 1. Klasyfikacja
**Cel** 
<table>
<tr>
<td>
Wykrywaj intencje użytkowników chatbota
</td>
</tr>
</table>
  
**Przykłady klas**<br/>
[Przykładowe źródło danych](https://github.com/spackows/CASCON-2017_Analyzing_chat/blob/master/sample-data/sample-NLC-training-data.csv)

Klasa: "cześć"
```
Cześć
Hej
Dobry wieczór
Dzień dobry
cześć dzień dobry
```
Klasa: "pytanie"
```
Cześć, chciałem wiedzieć, jak wyeksportować dane z notatników Pythona?
Cześć, czy mogę odzyskać usunięty notatnik?
Cześć, jak dodać folder plików do projektu?
Cześć drużyno Jak zmienić nazwę notebooka?
Jak przesłać zestaw danych z lokalnego do RStudio
Dzień dobry, czy możesz mi pomóc przesłać plik kształtu?
Jak zacząć tworzyć notatnik R?
```
Klasa: "problem"
```
Cześć, nie mogę się dzisiaj zalogować z powodu tego błędu. Konto właściciela jest nieaktywne. Może to być spowodowane wygaśnięciem członkostwa.
Nie mogę zarejestrować swojego konta, proszę o pomoc
Cześć, dostałem wiadomość, że nie udało się przygotować Object-Storage. Czy mógłbyś dać mi sugestię. Dziękuję.
Cześć, próbuję poprosić o nowy klucz dostępu API, ale nie wiem, jaki powinien być dla mnie identyfikator
Kiedy próbuję dodać model do dowolnego projektu, pojawia się błąd Nieautoryzowany.
```
**Dane wejściowe do testów**
```
Cześć Jest tam ktoś?
```
```
Masz problemy z konfiguracją usługi WML
```
```
Cześć zespole, jak mogę zaimportować dane do projektu?
```

Zobacz: [Przykładowa odpowiedź](prompt-engineering-exercise-answers.md#1-classify)

<p>&nbsp;</p>


## 2. Napisz od nowa
**Cel** 
<table>
<tr>
<td>
Przekształć Markdown do HTML
</td>
</tr>
</table>

**Markdown**
```
## Background
The [IBM Watson Natural Language Processing library](https://dataplatform.cloud.ibm.com/docs/
content/wsj/analyze-data/watson-nlp.html) to biblioteka Pythona, która udostępnia podstawowe elementy naturalne
przetwarzanie języka (NLP), takie jak analiza składni i ekstrakcja słów kluczowych z gotowymi rozwiązaniami,
wstępnie wytrenowane modele. Biblioteka Watson NLP ułatwia również dostosowywanie języka
modele ze słownikami terminów specyficznych dla Twojej domeny.
```
```
## Function
Korzystanie z LLM jest całkiem proste: poproś model tekstem (np. „Wziąłem psa”) i model
generuje tekst jako wyjście (np. "na spacer").
```
```
## Hall of shame: when LLMs go wrong
Nawet twórcy LLM nie zawsze mogą w pełni przewidzieć lub wyjaśnić dane wyjściowe tych modeli: 
[ChatGPT's creators can’t figure out why it won’t talk about Trump](https://www.semafor.com/
article/02/03/2023/how-chatgpt-inadvertently-learned-to-avoid-talking-about-trump)
```

Zobacz: [Przykładowa odpowiedź](prompt-engineering-exercise-answers.md#2-rewrite)

<p>&nbsp;</p>

## 3. Przewidywanie pytań
**Cel** 
<table>
<tr>
<td>
Utwórz listę pytań, które klient może mieć na temat jednego z podanych fragmentów tematycznych
</td>
</tr>
</table>

**Opisy posczególnych narzędzi**

[Tworzenie notebooków](https://dataplatform.cloud.ibm.com/docs/content/wsj/analyze-data/creating-notebooks.html)
```
Możesz dodać notatnik do swojego projektu, korzystając z jednej z następujących metod: tworząc plik notatnika,
skopiowanie przykładowego notatnika z Galerii lub dodanie notatnika z katalogu. Ty musisz mieć
rolę administratora lub redaktora w projekcie, aby utworzyć notatnik.
```
[Spark w RStudio](https://dataplatform.cloud.ibm.com/docs/content/wsj/analyze-data/rstudio-spark.html)
```
Chociaż środowiska uruchomieniowego RStudio IDE nie można uruchomić w środowisku uruchomieniowym platformy Spark ze środowiskiem R, można użyć
Spark w skryptach języka R i aplikacjach Shiny, uzyskując programowy dostęp do jądra platformy Spark. używa RStudio
pakiet sparklyr do łączenia się ze Spark z R. Pakiet sparklyr zawiera interfejs dplyr
do ramek danych Spark, a także interfejs R do rozproszonych potoków uczenia maszynowego Spark.
```
[Narzędzie AutoAI](https://dataplatform.cloud.ibm.com/docs/content/wsj/analyze-data/autoai-overview.html)
```
Graficzne narzędzie AutoAI w Watson Studio analizuje dane i wykrywa transformacje danych,
algorytmy i ustawienia parametrów, które najlepiej sprawdzają się w przypadku problemu z modelowaniem predykcyjnym. AutoAI
wyświetla wyniki jako modelowe potoki kandydatów uszeregowane na tablicy liderów do wyboru.
```

Zobacz: [Przykładowa odpowiedź](prompt-engineering-exercise-answers.md#3-study-questions)

<p>&nbsp;</p>


## 4. Ekstrakcja tekstu
**Cel** 
<table>
<tr>
<td>
Wyodrębnij imiona z jednego z tych zdań
</td>
</tr>
</table>

**Przykłady**
```
Gdy tylko Karolina oraz Ania spotkały się w parku, rzuciły się sobie 
w ramiona i zaczęły wspominać dawne lata szkolne.
```
```
Marcin i Michał, podczas pracy nad wspólnym projektem, szybko odkryli, 
że mają ze sobą wiele wspólnego, a łączy ich między innymi 
wspólna miłość do zwierząt i zafascynowanie wspinaniem.
```
```
Kiedy wyjrzałam przez okno, zobaczyłam, że moja dawna znajoma 
Diana, wróciła w rodzinne strony po wielu latach nieobecności.
```
```
Za każdym razem kiedy idę odebrać paczkę w pidżamie, 
liczę na to, że nikogo nie spotkam. Niestety, tym razem 
na mojej drodze stanął Marek, mój największy wróg.
```

Zobacz: [Przykładowa odpowiedź](prompt-engineering-exercise-answers.md#4-text-extraction)

<p>&nbsp;</p>

## 5. Sumaryzacja
**Cel** 
<table>
<tr>
<td>
Streść podany tekst
</td>
</tr>
</table>

**Przykłady**
```
Mały ptaszek ćwierkał, gdy zbierała w dziobie gałązki i kawałki mchu, odlatując i
dalej między drzewami. Z każdą podróżą jej gniazdo nabierało kształtu, stając się bardziej przytulne i zachęcające.
Wkrótce stworzyła przytulny dom, w którym wychowała swoje stado ćwierkających piskląt.
```
```
Gdy tylko opakowanie zostało otwarte, oczy małego kota zaświeciły się z podniecenia. Rzuciła się
na nowej zabawce, z radością miotając nią po pokoju. Z zadowolonym mruczeniem, ona
przytuliła się do swojej zabawki, czując wdzięczność za miłość i uwagę troskliwego właściciela.
```
```
Statek kołysał się i kołysał na wzburzonym morzu, gdy szalał sztorm. Fale wysokie jak góry
uderzył w kadłub, grożąc wywróceniem się statku. Ale kapitan i załoga wytrzymali
stabilnie, poruszając się po zdradzieckich wodach z wprawą i determinacją, aż w końcu
sztorm ucichł i statek wyłonił się triumfalnie, poobijany, ale nienaruszony.
```
```
Gdy tylko dwa psy spotkały się w parku, ich ogony zaczęły machać i skakały
siebie z radością. Ich właściciele nawiązali rozmowę i wkrótce okazało się, że tak
mają ze sobą wiele wspólnego, łącząc ich wspólną miłość do psów i na zewnątrz. Do końca
dnia zawiązały się nowe przyjaźnie i zarówno psy, jak i ich właściciele opuścili park
szczęśliwe serca i merdające ogony.
```