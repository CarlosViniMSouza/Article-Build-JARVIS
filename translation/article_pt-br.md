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

### The above command will create a virtual environment named `env`. Now, we need to activate the environment using the command:

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
