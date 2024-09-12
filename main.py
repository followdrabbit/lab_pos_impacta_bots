import argparse  # Biblioteca para lidar com argumentos da linha de comando
from openai import OpenAI  # Biblioteca da OpenAI para fazer as transcrições e traduções
from dotenv import load_dotenv  # Biblioteca para carregar variáveis de ambiente a partir de um arquivo .env
from docx import Document  # Biblioteca para criar e manipular documentos do Word (.docx)
from rich.console import Console  # Biblioteca Rich para melhorar a exibição no console
from rich.panel import Panel  # Usada para criar caixas de destaque no terminal

# Inicializa o console do Rich para exibir mensagens formatadas
console = Console()

# Função para transcrever o áudio no idioma original
def transcribe_audio(file_path):
    # Cria um cliente para interagir com a API da OpenAI
    client = OpenAI()
    
    # Abre o arquivo de áudio em modo leitura binária ("rb")
    with open(file_path, "rb") as audio_file:
        # Faz a transcrição do áudio utilizando o modelo "whisper-1"
        transcription = client.audio.transcriptions.create(
            model="whisper-1",  # Define o modelo de transcrição a ser usado
            file=audio_file      # Passa o arquivo de áudio para a transcrição
        )
    # Retorna o texto transcrito
    return transcription.text

# Função para traduzir o áudio transcrito para o inglês
def translate_audio(file_path):
    # Cria um cliente para interagir com a API da OpenAI
    client = OpenAI()
    
    # Abre o arquivo de áudio em modo leitura binária ("rb")
    with open(file_path, "rb") as audio_file:
        # Faz a tradução do áudio para o inglês utilizando o modelo "whisper-1"
        translation = client.audio.translations.create(
            model="whisper-1",  # Define o modelo de tradução a ser usado
            file=audio_file      # Passa o arquivo de áudio para a tradução
        )
    # Retorna o texto traduzido
    return translation.text

# Função para exportar a transcrição e tradução para um documento Word (.docx)
def export_to_docx(transcription_text, translation_text, output_path="transcription_and_translation.docx"):
    # Cria um novo documento do Word
    doc = Document()
    
    # Adiciona um título para a seção de transcrição no idioma original
    doc.add_heading('Transcrição no idioma original:', level=1)
    # Adiciona o texto transcrito ao documento como um parágrafo
    doc.add_paragraph(transcription_text)
    
    # Adiciona um título para a seção de tradução para o inglês
    doc.add_heading('Tradução para o inglês:', level=1)
    # Adiciona o texto traduzido ao documento como um parágrafo
    doc.add_paragraph(translation_text)
    
    # Salva o documento no caminho especificado (ou usa o padrão "transcription_and_translation.docx")
    doc.save(output_path)
    # Exibe uma mensagem de sucesso no terminal
    console.print(f"[green]Arquivo salvo com sucesso em: {output_path}[/green]")

# Parte principal do código, executada quando o script é rodado
if __name__ == "__main__":
    # Carrega as variáveis de ambiente do arquivo .env (como a chave da API da OpenAI)
    load_dotenv()  
    
    # Configura a análise de argumentos passados pela linha de comando
    parser = argparse.ArgumentParser(description="Transcrever e traduzir áudio usando a API da OpenAI")
    # Argumento obrigatório: caminho para o arquivo de áudio
    parser.add_argument("file_path", type=str, help="Caminho para o arquivo de áudio (ex: audio.mp3)")
    # Argumento opcional: caminho para o arquivo de saída (.docx)
    parser.add_argument("--output", type=str, default="transcription_and_translation.docx", 
                        help="Caminho para o arquivo de saída do .docx (padrão: transcription_and_translation.docx)")
    
    # Processa os argumentos fornecidos pelo usuário
    args = parser.parse_args()
    
    # Realiza a transcrição do áudio no idioma original
    transcription_text = transcribe_audio(args.file_path)
    # Exibe a transcrição no terminal usando uma caixa estilizada do Rich
    console.print(Panel.fit("[bold]Transcrição no idioma original:[/bold]\n" + transcription_text, 
                            title="Transcrição", subtitle="Idioma Original", border_style="blue"))
    
    # Realiza a tradução para o inglês
    translation_text = translate_audio(args.file_path)
    # Exibe a tradução no terminal usando uma caixa estilizada do Rich
    console.print(Panel.fit("[bold]Tradução para o inglês:[/bold]\n" + translation_text, 
                            title="Tradução", subtitle="Inglês", border_style="green"))
    
    # Exporta a transcrição e a tradução para um arquivo .docx
    export_to_docx(transcription_text, translation_text, args.output)
