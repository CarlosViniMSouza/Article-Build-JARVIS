# Isso é um resumo sobre *Projeto Python - Como construir o JARVIS de Tony Stark com Python*

## Artigo por: Ashutosh Krishna

![imgProject](https://www.freecodecamp.org/news/content/images/size/w2000/2021/12/png_20211209_232339_0000.png)

### Você se lembra de J.A.R.V.I.S., assistente pessoal virtual de Tony Stark? Se você já viu algum dos filmes do Ironman ou dos Vingadores, tenho certeza que sim.

### Você já se perguntou se poderia criar seu próprio assistente pessoal? Sim? Tony Stark pode nos ajudar com isso!

![imgTonyStark](https://www.freecodecamp.org/news/content/images/size/w1000/2021/12/tony-snap2_rv5gmh.jpg)

### Opa, você esqueceu que ele não existe mais? É triste que ele não possa mais nos salvar. Mas hey, sua linguagem de programação favorita Python pode ajudá-lo com isso.

### Sim, você ouviu direito. Podemos criar nosso próprio J.A.R.V.I.S. usando Python. Vamos mergulhar nisso!

## Configuração do Projeto:

### Enquanto você está codificando este projeto, você encontrará vários módulos e bibliotecas externas. Vamos aprender sobre eles e instalá-los. Mas antes de instalá-los, vamos criar um ambiente virtual e ativá-lo.

### Vamos criar um ambiente virtual usando o `virtualenv`. Python agora vem com uma biblioteca `virtualenv` pré-instalada. Assim, para criar um ambiente virtual, você pode usar o comando abaixo:

```shell
$ python -m venv env
```

### O comando acima criará um ambiente virtual chamado `env`. Agora, precisamos ativar o ambiente usando o comando:

```shell
$ . env/Scripts/activate
```

### Para verificar se o ambiente foi ativado ou não, você pode ver (env) em seu terminal. Agora podemos instalar as bibliotecas.

### 1. pyttsx3: pyttsx é uma biblioteca de texto para voz de plataforma cruzada que é independente de plataforma. A principal vantagem de usar esta biblioteca para conversão de texto em fala é que ela funciona offline. Para instalar este módulo, digite o comando abaixo no terminal:

```shell
$ pip install pyttsx3
```

### 2. SpeechRecognition: Isso nos permite converter áudio em texto para processamento posterior. Para instalar este módulo, digite o comando abaixo no terminal:

```shell
$ pip install SpeechRecognition
```

### 3. pywhatkit: Esta é uma biblioteca fácil de usar que nos ajudará a interagir com o navegador de maneira muito fácil. Para instalar o módulo, execute o seguinte comando no terminal:

```shell
$ pip install pywhatkit
```

### 4. wikipedia: Usaremos isso para obter uma variedade de informações no site da Wikipedia. Para instalar este módulo, digite o comando abaixo no terminal:

```shell
$ pip install wikipedia
```

### 5. requests: Esta é uma biblioteca HTTP elegante e simples para Python que permite enviar solicitações HTTP/1.1 com extrema facilidade. Para instalar o módulo, execute o seguinte comando no terminal:

```shell
$ pip install requests
```

## Arquivos .env:

### Precisamos desse arquivo para armazenar alguns dados privados, como chaves de API, senhas e assim por diante, que estão relacionados ao projeto. Por enquanto, vamos armazenar o nome do usuário e do bot.

### Crie um arquivo chamado .env e adicione o seguinte conteúdo lá:

```shell
USER=Ashutosh
BOTNAME=JARVIS
```

### Para usar o conteúdo do arquivo .env, instalaremos outro módulo chamado python-decouple como:

```shell
$ pip install python-decouple
```

### Saiba mais sobre variáveis de ambiente em Python [aqui](https://iread.ga/posts/49/do-you-really-need-environment-variables-in-python).

## Como configurar o JARVIS com Python:

### Antes de começarmos a definir algumas funções importantes, vamos primeiro criar um mecanismo de fala.

```Python
import pyttsx3
from decouple import config

USERNAME = config('USER')
BOTNAME = config('BOTNAME')


engine = pyttsx3.init('sapi5')

# Set Rate
engine.setProperty('rate', 190)

# Set Volume
engine.setProperty('volume', 1.0)

# Set Voice (Female)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
```

### Vamos analisar o script acima. Em primeiro lugar, inicializamos um `engine` usando o módulo `pyttsx3`. `sapi5` é uma API de fala da Microsoft que nos ajuda a usar as vozes. Saiba mais sobre isso aqui.

### Em seguida, estamos definindo as propriedades de `rate` e `volume` do mecanismo de fala usando o método `setProperty`.

### Agora, podemos obter as vozes do mecanismo usando o método `getProperty`. `voices` será uma lista de vozes disponíveis em nosso sistema. Se nós imprimi-lo, podemos ver como abaixo:

```shell
[<pyttsx3.voice.Voice object at 0x000001AB9FB834F0>, <pyttsx3.voice.Voice object at 0x000001AB9FB83490>]
```

### O primeiro é uma voz masculina e o outro é uma voz feminina. JARVIS era um assistente do sexo masculino nos filmes, mas eu escolhi definir a propriedade de `voice` como feminina para este tutorial usando o método `setProperty`.

```Markdown
Nota: Se você receber um erro relacionado ao PyAudio, baixe o PyAudio wheel [aqui](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio) e instale-o dentro do ambiente virtual.
```

### Além disso, usando o método de `config` do desacoplamento, estamos obtendo o valor de `USER` e `BOTNAME` das variáveis de ambiente.

## Habilite a função de falar

### A função speak será responsável por falar qualquer texto que for passado a ela. Vamos ver o código:

```python
# Conversão de texto em fala
def speak(text):
    # Usado para falar qualquer texto que seja passado a ele
    
    engine.say(text)
    engine.runAndWait()
```

### No método `speak()`, o mecanismo fala qualquer texto que for passado a ele usando o método `say()`. Usando o método `runAndWait()`, ele bloqueia durante o loop de eventos e retorna quando a fila de comandos é limpa.

## Habilite a função Saudação:

### Esta função será usada para saudar o usuário sempre que o programa for executado. De acordo com o horário atual, ele cumprimenta Bom dia, Boa tarde ou Boa noite ao usuário.

```python
from datetime import datetime

def greet_user():
    """Greets the user according to the time"""
    
    hour = datetime.now().hour
    if (hour >= 6) and (hour < 12):
        speak(f"Bom Dia {USERNAME}")
    elif (hour >= 12) and (hour < 16):
        speak(f"Boa Tarde {USERNAME}")
    elif (hour >= 16) and (hour < 19):
        speak(f"Boa Noite {USERNAME}")
    speak(f"Eu sou {BOTNAME}. Como posso te ajudar?")
```

### Primeiramente, obtemos a hora atual, ou seja, se a hora atual for 11h15, a hora será 11. Se o valor da hora estiver entre 6 e 12, deseje bom dia ao usuário. Se o valor for entre 12 e 16, deseje Boa Tarde e da mesma forma, se o valor for entre 16 e 19, deseje Boa Noite. Estamos usando o método speak para falar com o usuário.

## Como obter a opinião do usuário:

### Usamos esta função para receber os comandos do usuário e reconhecer o comando usando o módulo `speech_recognition`.

```python
import speech_recognition as sr
from random import choice
from utils import opening_text


def take_user_input():
    # Recebe a entrada do usuário, reconhece-a usando o módulo de reconhecimento de fala e a converte em texto:

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Ouvindo....')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Reconhecendo...')
        query = r.recognize_google(audio, language='en-in')
        if not 'exit' in query or 'stop' in query:
            speak(choice(opening_text))
        else:
            hour = datetime.now().hour
            if 21 <= hour < 6:
                speak("Boa Noite Senhor, tenha cuidado!")
            else:
                speak('Tenha um bom dia senhor!')
            exit()
    except Exception:
        speak('Desculpe-me, mas não consegui entender. Poderias dizer novamente?')
        query = 'Nada'
    return query
```

### Importamos o módulo `speech_recognition` como `sr`. A classe Recognizer no módulo `speech_recognition` nos ajuda a reconhecer o áudio. O mesmo módulo possui uma classe Microfone que nos dá acesso ao microfone do dispositivo. Assim, com o microfone como `source`, tentamos ouvir o áudio usando o método `listen()` na classe _Recognizer_.

### Também definimos `pause_threshold` como 1, ou seja, ele não reclamará mesmo se fizermos uma pausa de um segundo enquanto falamos.

### A seguir, usando o método `reconhec_google()` da classe _Recognizer_, tentamos reconhecer o áudio. O método `reconhece_google()` realiza o reconhecimento de fala no áudio transmitido a ele, usando a **API de reconhecimento de fala do Google**.

### Definimos o idioma para `en-in`, que é o inglês da Índia. Ele retorna a transcrição do áudio, que nada mais é do que uma string. Nós o armazenamos em uma variável chamada `querry`.

### Se a consulta tiver palavras de `exit` ou de `stop`, significa que estamos pedindo ao assistente para parar imediatamente. Portanto, antes de parar, cumprimentamos o usuário novamente de acordo com a hora atual. Se estiver entre 21 e 6, deseje _Boa Noite_ ao usuário, senão, alguma outra mensagem.

### Nós criamos um arquivo `utils.py` que tem apenas uma lista contendo algumas declarações como esta:

```python
opening_text = [
    "Legal, já estou tratando disso, senhor.",
    "Ok, senhor, estou trabalhando nisso.",
    "Só um segundo senhor.",
]
```

### Se a consulta não tiver essas duas palavras (sair ou parar), falamos algo para dizer ao usuário que as ouvimos. Para isso, usaremos o método de escolha do módulo aleatório para selecionar aleatoriamente qualquer instrução da lista `opening_text`. Depois de falar, saímos do programa.

### Durante todo o processo, se encontrarmos uma exceção, pedimos desculpas ao usuário e definimos a `querry` a como Nenhum. No final, retornamos a `querry`.

## Como configurar funções offline:

### Dentro da pasta de `functions`, crie um arquivo Python chamado `os_ops.py`. Neste arquivo, vamos criar várias funções para interagir com o sistema operacional.

```Python
import os
import subprocess as sp

paths = {
    'notepad': "C:\\Program Files\\Notepad++\\notepad++.exe",
    'Visual Studio': "C:\\Program Files (x86)\\Microsoft Visual Studio\\Installer\\setup",
    'calculator': "C:\\Windows\\System32\\calc.exe"
}
```

### No script acima, criamos um dicionário chamado `paths` que tem o nome do software como chave e seu caminho como valor. Você pode alterar os caminhos de acordo com seu sistema e adicionar mais caminhos de software, se necessário.

## Como abrir a câmera:

### Usaremos esta função para abrir a câmera em nosso sistema. Estaremos usando o módulo de `subprocess` para executar o comando.

```python
def open_camera():
    sp.run('start microsoft.windows.camera:', shell=True)
```

## Como abrir o bloco de notas e o Discord:

### Usaremos essas funções para abrir o Notepad ++ e o Discord no sistema.

```python
def open_notepad():
    os.startfile(paths['notepad'])


def open_discord():
    os.startfile(paths['discord'])
```

## Como abrir o prompt de comando:

### Usaremos esta função para abrir o prompt de comando em nosso sistema.

```python
def open_cmd ():
    os.system('cmd inicial')
```

## Como abrir a calculadora:

### Usaremos esta função para abrir a calculadora em nosso sistema.

```python
def open_calculator():
    sp.Popen(paths['calculator'])
```

## Estaremos adicionando várias funções online. Eles são:

1 - Encontre meu endereço IP

2 - Pesquise na Wikipedia

3 - Reproduza vídeos no YouTube

4 - Pesquise no Google

5 - Enviar mensagem WhatsApp

6 - Enviar email

7 - Obtenha as últimas manchetes de notícias

8 - Obtenha o boletim meteorológico

9 - Obtenha filmes populares

10 - Piadas aleatórias

11 - Obtenha conselhos aleatórios

### Vamos criar um arquivo chamado `online_ops.py` dentro do diretório de `functions` e começar a criar essas funções uma após a outra. Por enquanto, adicione o seguinte código ao arquivo:

```python
import requests
import wikipedia
import pywhatkit as kit
from email.message import EmailMessage
import smtplib
from decouple import config
```

### Antes de começarmos a trabalhar com APIs, se você não estiver familiarizado com APIs e como interagir com elas usando Python, confira este [tutorial](https://iread.ga/posts/26/python-api-tutorial).

## Como adicionar a função Find my IP Address:

### [ipify](https://www.ipify.org/) fornece uma API de endereço IP público simples. Só precisamos fazer uma solicitação GET neste URL: https://api64.ipify.org/?format=json. Ele retorna dados JSON como:

```json
{
  "ip": "117.214.111.199"
}
```

### Podemos então simplesmente retornar o `ip` dos dados JSON. Então, vamos criar este método:

```python
def find_my_ip():
    ip_address = requests.get('https://api64.ipify.org?format=json').json()
    return ip_address["ip"]
```

## Como adicionar a função Pesquisar na Wikipedia:

### Para pesquisar na Wikipedia, usaremos o módulo da `wikipedia` que instalamos anteriormente neste tutorial.

```python
def search_on_wikipedia(query):
    results = wikipedia.summary(query, sentences=2)
    return results
```

### Dentro do módulo da `wikipedia`, temos um método `summary()` que aceita uma consulta como argumento. Além disso, também podemos passar o número de frases necessárias. Então, simplesmente retornamos o resultado.
