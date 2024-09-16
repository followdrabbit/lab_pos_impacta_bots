# Transcrição e Tradução de Áudio com OpenAI Whisper

Este projeto utiliza o modelo Whisper da OpenAI para transcrever arquivos de áudio e traduzi-los para o inglês. O fluxo completo começa com a conversão de um arquivo de texto para áudio utilizando a API **OpenAI TTS**. O áudio gerado é enviado à OpenAI para ser transcrito e, posteriormente, traduzido para o inglês. O resultado é salvo em um arquivo Word (.docx).

## Funcionalidades

- **Conversão de texto para áudio**: O texto fornecido é convertido em um arquivo de áudio `.mp3` utilizando a API TTS da OpenAI.
- **Transcrição de áudio**: O áudio gerado é transcrito no idioma original usando o modelo Whisper da OpenAI.
- **Tradução para o inglês**: A transcrição é traduzida diretamente para o inglês (EN-US).
- **Exportação para Word**: O resultado da transcrição e da tradução é exportado para um arquivo `.docx`.
- **Exibição estilizada no terminal**: Utiliza a biblioteca **Rich** para uma exibição visual aprimorada dos resultados no terminal.

## Requisitos

- **Python 3.6+**
- **Chave de API da OpenAI**: Para utilizar a transcrição e tradução, é necessário gerar uma chave da API da OpenAI. O uso da API pode gerar custos, dependendo do volume de requisições. Para mais informações sobre como gerar sua chave da API, consulte o [post no blog da Asimov Academy](https://hub.asimov.academy/blog/openai-api/).
- **Pacotes Python listados em `requirements.txt`**.

## Custos com a API

A utilização da API da OpenAI pode gerar custos conforme a quantidade de requisições realizadas para transcrição e tradução de áudio. Certifique-se de verificar a [política de preços da OpenAI](https://openai.com/pricing) antes de usar o serviço para evitar cobranças inesperadas.

## Instalação

1 **Clone o repositório** (ou baixe o código fonte):

```bash
git clone https://github.com/seu-usuario/nome-do-repositorio.git
cd nome-do-repositorio
```

2 **Crie um ambiente virtual** (opcional, mas recomendado):

```bash
python -m venv venv
venv\Scripts\activate   # Para Windows
```

3 **Instale as dependências**:

Execute o seguinte comando para instalar todas as bibliotecas necessárias:

```bash
pip install -r requirements.txt
```

4 **Configuração do arquivo `.env`**:

- No diretório do projeto, você encontrará um arquivo chamado `.env_renomear`.
- Renomeie esse arquivo para `.env`:

```bash
mv .env_renomear .env  # Ou renomeie manualmente no Windows
```

- Abra o arquivo `.env` e adicione sua chave de API da OpenAI na variável `OPENAI_API_KEY`:

```bash
OPENAI_API_KEY="SUA_CHAVE_DA_OPENAI_AQUI"
```

## Uso

Para executar o script, você deve fornecer o caminho para o arquivo de texto de entrada e, opcionalmente, os nomes para o arquivo de áudio e o arquivo de saída Word:

```bash
python main.py -f "caminho/para/arquivo/texto.txt" -o "caminho/para/arquivo/audio.mp3" -d "caminho/para/arquivo/resultado.docx"
```

- **-f, --file**: Caminho para o arquivo de texto de entrada.
- **-o, --output_audio**: Caminho para o arquivo de áudio gerado (padrão: `output_audio.mp3`).
- **-d, --output_docx**: Caminho para o arquivo de saída no formato `.docx` (padrão: `transcription_and_translation.docx`).
- **--model**: Modelo de TTS da OpenAI a ser utilizado (padrão: `tts-1`).
- **--voice**: Voz a ser usada para gerar o áudio (padrão: `alloy`).

> Mais opções de vozes e formatos podem ser encontradas na [documentação da API da OpenAI](https://platform.openai.com/docs/api-reference/audio/createSpeech).

### Exemplo de uso

```bash
python main.py -f "meutexto.txt" -o "meuaudio.mp3" -d "meuresultado.docx" --model "tts-1" --voice "nova"
```

Esse comando:

1. Lê o arquivo de texto `meutexto.txt`.
2. Converte o texto em áudio e salva como `meuaudio.mp3`.
3. Envia o áudio para a OpenAI para transcrição e tradução.
4. Salva a transcrição e a tradução no arquivo Word `meuresultado.docx`.

## Output

- O script exibirá a transcrição e a tradução diretamente no terminal, com uma formatação visual estilizada usando a biblioteca **Rich**.
- O resultado será salvo em um arquivo `.docx` com duas seções:
  1. **Transcrição no idioma original**.
  2. **Tradução para o inglês (EN-US)**.

## Estrutura do Projeto

- `main.py`: Script principal que faz a conversão de texto para áudio, transcrição, tradução e exportação.
- `requirements.txt`: Arquivo com todas as dependências necessárias para o projeto.
- `env_renomear`: Arquivo modelo onde você deve inserir sua chave de API da OpenAI. Renomeie para `.env` e edite conforme necessário.

## Licença

Este projeto está licenciado sob a licença MIT. Consulte o arquivo [LICENSE](LICENSE) para mais detalhes.