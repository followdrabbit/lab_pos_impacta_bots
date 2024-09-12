# Transcrição e Tradução de Áudio com OpenAI Whisper

Este projeto utiliza o modelo Whisper da OpenAI para transcrever arquivos de áudio e traduzi-los para o inglês. O script aceita um arquivo de áudio como entrada e gera tanto a transcrição no idioma original quanto a tradução para o inglês. O resultado pode ser salvo em um arquivo Word (.docx).

## Funcionalidades

- **Transcrição de áudio**: Transcreve o conteúdo do áudio no idioma original.
- **Tradução para o inglês**: Traduz o áudio transcrito diretamente para o inglês.
- **Exportação para Word**: Exporta o resultado da transcrição e da tradução para um arquivo `.docx`.
- **Exibição estilizada no terminal**: Exibe a transcrição e a tradução no terminal com formatação visual agradável usando a biblioteca `rich`.

## Requisitos

- **Python 3.6+**
- **Chave de API da OpenAI**: Para utilizar este script, é necessário gerar uma chave da API da OpenAI. O uso da API pode gerar custos, dependendo do volume de requisições. Para mais informações sobre como gerar sua chave da API, consulte o [post no blog da Asimov Academy](https://hub.asimov.academy/blog/openai-api/).
- Pacotes Python listados em `requirements.txt`.

## Custos com a API

A utilização da API da OpenAI não é gratuita e pode gerar custos conforme a quantidade de requisições realizadas para transcrição e tradução de áudio. Certifique-se de verificar a [política de preços da OpenAI](https://openai.com/pricing) antes de usar o serviço para evitar cobranças inesperadas.

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

- No diretório do projeto, você encontrará um arquivo chamado `env_renomear`.
- Renomeie esse arquivo para `.env`:

```bash
mv env_renomear .env  # Ou renomeie manualmente no Windows
```

- Abra o arquivo `.env` e adicione sua chave de API da OpenAI na variável `OPENAI_API_KEY`:

```bash
OPENAI_API_KEY="SUA_CHAVE_DA_OPENAI_AQUI"
```

## Uso

Para executar o script, você deve fornecer o caminho para o arquivo de áudio e, opcionalmente, um nome para o arquivo de saída do Word:

```bash
python main.py "caminho/para/arquivo/audio.mp3" --output "nome_do_arquivo.docx"
```

- **file_path**: Caminho para o arquivo de áudio que será transcrito e traduzido.
- **--output** (opcional): Nome do arquivo de saída no formato `.docx`. Se não for especificado, o nome padrão será `transcription_and_translation.docx`.

### Exemplo de uso

```bash
python main.py "audio.mp3" --output "resultado.docx"
```

## Output

- O script exibirá a transcrição e a tradução diretamente no terminal, com uma formatação visual estilizada.
- O resultado será salvo em um arquivo `.docx` com duas seções:
  1. **Transcrição no idioma original**.
  2. **Tradução para o inglês**.

## Estrutura do Projeto

- `main.py`: Script principal que faz a transcrição, tradução e exportação.
- `requirements.txt`: Arquivo com todas as dependências necessárias para o projeto.
- `.env_renomear`: Arquivo modelo onde você deve inserir sua chave de API da OpenAI. Renomeie para `.env` e edite conforme necessário.

## Licença

Este projeto está licenciado sob a licença MIT. Consulte o arquivo [LICENSE](LICENSE) para mais detalhes.