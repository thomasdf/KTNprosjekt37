# fellesProsjekt37
#### Fellesprosjekt Gruppe 37: Dag Erik Homdrum Løvgren, Daniel lines, Lars Moe Ellefsen, Oscar Thån Conrad, Thomas Drabløs Frøysa.

## Git-kommandoer
#### Skrevet med tanke på en linux-maskin.
* Klone repository:
	* Finn et directory der du vil opprette din lokale klone av prosjektet
	* `git clone https://github.com/thomasdf/fellesProsjekt37.git`
	* evt. `git@github.com:thomasdf/fellesProsjekt37.git` hvis du bruker SSH
* Oppdatere repository:
	* **Pass på at du er i master!**
	* `git pull origin`
	* *Husk å oppdatere regelmessig*
* **Liste branches:**
	* **`git branch` for lokale branches**
	* `git branch -r` for å vise remote branches
	* `git branch -a` for å også vise remote branches i repoen
* **Sjekke status på branchen/commiten du jobber i:**
	* **`git status`**
* **Sjekke commit-loggen på branchen du er i:**
	* **`git log`**
* Lage ny branch:
	* `git branch <ny_branch_navn>`
* Bytte branch:
	* `git checkout <branch_navn>`
* Commite til repoen:
	1. **Sjekk at du er på rett branch!**
	* `git add -A` eller `git add --all` legger til alle filene du har laget/modifisert i commiten din. Ofte fungerer og `git add .`, men noen ganger er ikke det tilstrekkelig.
	* `git commit -m "<commit-message>"` commiter (dvs. lager et checkpoint) med alle filene du added til commiten på denne branchen
	* `git push --set-upstream origin <branch_navn>` pusher branchen med commiten din opp til GitHub
	* Gå til GitHub, og så vil du se at branchen din er blitt lagt til. Trykk så på "Compare & pull request" for å forespør at branchen din skal merges inn i master

## Konvensjoner
* Git:
	* Branch ALLTID fra master
	* Aldri push direkte på master, push din egen branch til GitHub og lag et pull-request som forklart over
	* Commit så mye du vil (checkpoints), men vær sikker på at det du har gjort er funksjonelt før du pusher det
	* Commit-messages:
		* Skal helst skrives på norsk
		* Du kan enten skrive `git commit -m "<melding>"`, eller du kan skrive `git commit` og skrive meldingen din i en teksteditor. Meldingene du skriver etter "-m" i commitsa bør uansett være på en av disse to formene:
			1. En linje med kort beskrivelse av hva du har endret/lagt til, ex `git commit -m "Endret readme-en"`
			* En linje med kort beskrivelse, så dobbelt linjeskift (SHIFT+ENTER i bash) etterfulgt av en mer in-depth beskrivelse, ex:
				* `git commit -m "Endret readme-en`
				* `<tom linje>`
				* `Har endret readme-en for å reflektere de endringer vi har gjort i prosjektet."`
* Java:
	* Skriv klasser med stor forbokstav, ex "MyClass.java"
	* Skriv funksjoner med liten forbokstav, og stor bokstav for hvert nytt ord, ex "myFunction()"
	* Skriv variabelnavn med små bokstaver og understretk, ex. "my_variable"
* Div:
	* Skriv FXML-filer med stor forbokstav, som en klasse, ex "MyFXMLView.fxml"
	* Skriv CSS-filer som en variabel, små bokstaver og understrek, ex "my_style.css"
