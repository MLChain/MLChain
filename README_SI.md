![cover-v5-optimized](https://github.com/mlchain/mlchain/assets/13230914/f9e19af5-61ba-4119-b926-d10c4c06ebab)

<p align="center">
  📌 <a href="https://mlchain.khulnasoft.com/blog/introducing-mlchain-workflow-file-upload-a-demo-on-ai-podcast">Predstavljamo nalaganje datotek Mlchain Workflow: znova ustvarite Google NotebookLM Podcast</a>
</p>

<p align="center">
  <a href="https://cloud-mlchain.khulnasoft.com">Mlchain Cloud</a> ·
  <a href="https://docs-mlchain.khulnasoft.com/getting-started/install-self-hosted">Samostojno gostovanje</a> ·
  <a href="https://docs-mlchain.khulnasoft.com">Dokumentacija</a> ·
  <a href="https://umlchain.app/chat/22L1zSxg6yW1cWQg">Povpraševanje za podjetja</a>
</p>

<p align="center">
    <a href="https://mlchain.khulnasoft.com" target="_blank">
        <img alt="Static Badge" src="https://img.shields.io/badge/Product-F04438"></a>
    <a href="https://mlchain.khulnasoft.com/pricing" target="_blank">
        <img alt="Static Badge" src="https://img.shields.io/badge/free-pricing?logo=free&color=%20%23155EEF&label=pricing&labelColor=%20%23528bff"></a>
    <a href="https://discord.gg/FngNHpbcY7" target="_blank">
        <img src="https://img.shields.io/discord/1082486657678311454?logo=discord&labelColor=%20%235462eb&logoColor=%20%23f5f5f5&color=%20%235462eb"
            alt="chat on Discord"></a>
    <a href="https://twitter.com/intent/follow?screen_name=mlchain_ai" target="_blank">
        <img src="https://img.shields.io/twitter/follow/mlchain_ai?logo=X&color=%20%23f5f5f5"
            alt="follow on X(Twitter)"></a>
    <a href="https://hub.docker.com/u/mlchain" target="_blank">
        <img alt="Docker Pulls" src="https://img.shields.io/docker/pulls/mlchain/mlchain-web?labelColor=%20%23FDB062&color=%20%23f79009"></a>
    <a href="https://github.com/mlchain/mlchain/graphs/commit-activity" target="_blank">
        <img alt="Commits last month" src="https://img.shields.io/github/commit-activity/m/mlchain/mlchain?labelColor=%20%2332b583&color=%20%2312b76a"></a>
    <a href="https://github.com/mlchain/mlchain/" target="_blank">
        <img alt="Issues closed" src="https://img.shields.io/github/issues-search?query=repo%3Amlchain%2Fmlchain%20is%3Aclosed&label=issues%20closed&labelColor=%20%237d89b0&color=%20%235d6b98"></a>
    <a href="https://github.com/mlchain/mlchain/discussions/" target="_blank">
        <img alt="Discussion posts" src="https://img.shields.io/github/discussions/mlchain/mlchain?labelColor=%20%239b8afb&color=%20%237a5af8"></a>
</p>

<p align="center">
  <a href="./README.md"><img alt="README in English" src="https://img.shields.io/badge/English-d9d9d9"></a>
  <a href="./README_CN.md"><img alt="简体中文版自述文件" src="https://img.shields.io/badge/简体中文-d9d9d9"></a>
  <a href="./README_JA.md"><img alt="日本語のREADME" src="https://img.shields.io/badge/日本語-d9d9d9"></a>
  <a href="./README_ES.md"><img alt="README en Español" src="https://img.shields.io/badge/Español-d9d9d9"></a>
  <a href="./README_FR.md"><img alt="README en Français" src="https://img.shields.io/badge/Français-d9d9d9"></a>
  <a href="./README_KL.md"><img alt="README tlhIngan Hol" src="https://img.shields.io/badge/Klingon-d9d9d9"></a>
  <a href="./README_KR.md"><img alt="README in Korean" src="https://img.shields.io/badge/한국어-d9d9d9"></a>
  <a href="./README_AR.md"><img alt="README بالعربية" src="https://img.shields.io/badge/العربية-d9d9d9"></a>
  <a href="./README_TR.md"><img alt="Türkçe README" src="https://img.shields.io/badge/Türkçe-d9d9d9"></a>
  <a href="./README_VI.md"><img alt="README Tiếng Việt" src="https://img.shields.io/badge/Ti%E1%BA%BFng%20Vi%E1%BB%87t-d9d9d9"></a>
  <a href="./README_SI.md"><img alt="README Slovenščina" src="https://img.shields.io/badge/Sloven%C5%A1%C4%8Dina-d9d9d9"></a>
</p>


Mlchain je odprtokodna platforma za razvoj aplikacij LLM. Njegov intuitivni vmesnik združuje agentski potek dela z umetno inteligenco, cevovod RAG, zmogljivosti agentov, upravljanje modelov, funkcije opazovanja in več, kar vam omogoča hiter prehod od prototipa do proizvodnje. 

## Hitri začetek
> Preden namestite Mlchain, se prepričajte, da vaša naprava izpolnjuje naslednje minimalne sistemske zahteve:
> 
>- CPU >= 2 Core
>- RAM >= 4 GiB

</br>

Najlažji način za zagon strežnika Mlchain je prek docker compose . Preden zaženete Mlchain z naslednjimi ukazi, se prepričajte, da sta Docker in Docker Compose nameščena na vašem računalniku:

```bash
cd mlchain
cd docker
cp .env.example .env
docker compose up -d
```

Po zagonu lahko dostopate do nadzorne plošče Mlchain v brskalniku na [http://localhost/install](http://localhost/install) in začnete postopek inicializacije.

#### Iskanje pomoči
Prosimo, glejte naša pogosta vprašanja [FAQ](https://docs-mlchain.khulnasoft.com/getting-started/install-self-hosted/faqs) če naletite na težave pri nastavitvi Mlchain. Če imate še vedno težave, se obrnite na [skupnost ali nas](#community--contact).

> Če želite prispevati k Mlchainju ali narediti dodaten razvoj, glejte naš vodnik za [uvajanje iz izvorne kode](https://docs-mlchain.khulnasoft.com/getting-started/install-self-hosted/local-source-code)

## Ključne značilnosti
**1. Potek dela**: 
  Zgradite in preizkusite zmogljive poteke dela AI na vizualnem platnu, pri čemer izkoristite vse naslednje funkcije in več.


  https://github.com/mlchain/mlchain/assets/13230914/356df23e-1604-483d-80a6-9517ece318aa



**2. Celovita podpora za modele**: 
  Brezhibna integracija s stotinami lastniških/odprtokodnih LLM-jev ducatov ponudnikov sklepanja in samostojnih rešitev, ki pokrivajo GPT, Mistral, Llama3 in vse modele, združljive z API-jem OpenAI. Celoten seznam podprtih ponudnikov modelov najdete [tukaj](https://docs-mlchain.khulnasoft.com/getting-started/readme/model-providers).

![providers-v5](https://github.com/mlchain/mlchain/assets/13230914/5a17bdbe-097a-4100-8363-40255b70f6e3)


**3. Prompt IDE**: 
  intuitivni vmesnik za ustvarjanje pozivov, primerjavo zmogljivosti modela in dodajanje dodatnih funkcij, kot je pretvorba besedila v govor, aplikaciji, ki temelji na klepetu. 

**4. RAG Pipeline**: 
  E Obsežne zmogljivosti RAG, ki pokrivajo vse od vnosa dokumenta do priklica, s podporo za ekstrakcijo besedila iz datotek PDF, PPT in drugih običajnih formatov dokumentov.

**5. Agent capabilities**: 
  definirate lahko agente, ki temeljijo na klicanju funkcij LLM ali ReAct, in dodate vnaprej izdelana orodja ali orodja po meri za agenta. Mlchain ponuja več kot 50 vgrajenih orodij za agente AI, kot so Google Search, DALL·E, Stable Diffusion in WolframAlpha.

**6. LLMOps**: 
  Spremljajte in analizirajte dnevnike aplikacij in učinkovitost skozi čas. Pozive, nabore podatkov in modele lahko nenehno izboljšujete na podlagi proizvodnih podatkov in opomb.

**7. Backend-as-a-Service**: 
  AVse ponudbe Mlchainja so opremljene z ustreznimi API-ji, tako da lahko Mlchain brez težav integrirate v svojo poslovno logiko.


## Uporaba Mlchain

- **Cloud </br>**
Gostimo storitev Mlchain Cloud za vsakogar, ki jo lahko preizkusite brez nastavitev. Zagotavlja vse zmožnosti različice za samostojno namestitev in vključuje 200 brezplačnih klicev GPT-4 v načrtu peskovnika.

- **Self-hosting Mlchain Community Edition</br>**
Hitro zaženite Mlchain v svojem okolju s tem [začetnim vodnikom](#quick-start) . Za dodatne reference in podrobnejša navodila uporabite našo [dokumentacijo](https://docs-mlchain.khulnasoft.com) .


- **Mlchain za podjetja/organizacije</br>**
Ponujamo dodatne funkcije, osredotočene na podjetja. Zabeležite svoja vprašanja prek tega klepetalnega robota ali nam pošljite e-pošto, da se pogovorimo o potrebah podjetja. </br>
  > Za novoustanovljena podjetja in mala podjetja, ki uporabljajo AWS, si oglejte Mlchain Premium na AWS Marketplace in ga z enim klikom uvedite v svoj AWS VPC. To je cenovno ugodna ponudba AMI z možnostjo ustvarjanja aplikacij z logotipom in blagovno znamko po meri.


## Staying ahead

Star Mlchain on GitHub and be instantly notified of new releases.

![star-us](https://github.com/mlchain/mlchain/assets/13230914/b823edc1-6388-4e25-ad45-2f6b187adbb4)


## Napredne nastavitve

Če morate prilagoditi konfiguracijo, si oglejte komentarje v naši datoteki .env.example in posodobite ustrezne vrednosti v svoji .env datoteki. Poleg tega boste morda morali prilagoditi docker-compose.yamlsamo datoteko, na primer spremeniti različice slike, preslikave vrat ali namestitve nosilca, glede na vaše specifično okolje in zahteve za uvajanje. Po kakršnih koli spremembah ponovno zaženite docker-compose up -d. Celoten seznam razpoložljivih spremenljivk okolja najdete tukaj .

Če želite konfigurirati visoko razpoložljivo nastavitev, so na voljo Helm Charts in datoteke YAML, ki jih prispeva skupnost, ki omogočajo uvedbo Mlchainja v Kubernetes.

- [Helm Chart by @LeoQuote](https://github.com/douban/charts/tree/master/charts/mlchain)
- [Helm Chart](https://github.com/MLChain/mlchain-helm)
- [YAML file](https://github.com/MLChain/mlchain-kubernetes)

#### Uporaba Terraform za uvajanje

namestite Mlchain v Cloud Platform z enim klikom z uporabo [terraform](https://www.terraform.io/)

##### Azure Global
- [Azure Terraform](https://github.com/MLChain/mlchain-azure-terraform)

##### Google Cloud
- [Google Cloud Terraform by @sotazum](https://github.com/DeNA/mlchain-google-cloud-terraform)

## Prispevam

Za tiste, ki bi radi prispevali kodo, si oglejte naš vodnik za prispevke . Hkrati vas prosimo, da podprete Mlchain tako, da ga delite na družbenih medijih ter na dogodkih in konferencah. 



> Iščemo sodelavce za pomoč pri prevajanju Mlchainja v jezike, ki niso mandarinščina ali angleščina. Če želite pomagati, si oglejte i18n README za več informacij in nam pustite komentar v global-userskanalu našega strežnika skupnosti Discord .

## Skupnost in stik

* [Github Discussion](https://github.com/mlchain/mlchain/discussions). Najboljše za: izmenjavo povratnih informacij in postavljanje vprašanj.
* [GitHub Issues](https://github.com/mlchain/mlchain/issues). Najboljše za: hrošče, na katere naletite pri uporabi MlChain, in predloge funkcij. Oglejte si naš [vodnik za prispevke](https://github.com/mlchain/mlchain/blob/main/CONTRIBUTING.md).
* [Discord](https://discord.gg/FngNHpbcY7). Najboljše za: deljenje vaših aplikacij in druženje s skupnostjo.
* [X(Twitter)](https://twitter.com/mlchain_ai). Najboljše za: deljenje vaših aplikacij in druženje s skupnostjo.

**Contributors**

<a href="https://github.com/mlchain/mlchain/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=mlchain/mlchain" />
</a>

## Star history

[![Star History Chart](https://api.star-history.com/svg?repos=mlchain/mlchain&type=Date)](https://star-history.com/#mlchain/mlchain&Date)


## Varnostno razkritje

Zaradi zaščite vaše zasebnosti se izogibajte objavljanju varnostnih vprašanj na GitHub. Namesto tega pošljite vprašanja na security@mlchain.khulnasoft.com in zagotovili vam bomo podrobnejši odgovor.

## Licenca

To skladišče je na voljo pod [odprtokodno licenco Mlchain](LICENSE) , ki je v bistvu Apache 2.0 z nekaj dodatnimi omejitvami.