import argparse
import os
from gtts import gTTS  # Biblioteca para converter texto em fala
from openai import OpenAI
from dotenv import load_dotenv
from docx import Document
from rich.console import Console
from rich.panel import Panel

# Inicializa o console do Rich para exibir mensagens formatadas
console = Console()

# Função para converter texto em áudio usando gTTS
def text_to_speech(text, output_audio_path):
    # Usa gTTS para converter o texto em áudio (formato mp3)
    tts = gTTS(text, lang='pt')  # 'pt' para português, troque se precisar de outro idioma
    tts.save(output_audio_path)
    console.print(f"[green]Áudio salvo em: {output_audio_path}[/green]")

# Função para enviar áudio para a OpenAI e obter a transcrição
def transcribe_audio(file_path):
    client = OpenAI()

    # Abre o arquivo de áudio no modo de leitura binária
    with open(file_path, "rb") as audio_file:
        transcription = client.audio.transcriptions.create(
            model="whisper-1",
            file=audio_file
        )
    return transcription.text

# Função para enviar áudio para a OpenAI e obter a tradução para o inglês
def translate_audio(file_path):
    client = OpenAI()

    # Abre o arquivo de áudio no modo de leitura binária
    with open(file_path, "rb") as audio_file:
        translation = client.audio.translations.create(
            model="whisper-1",
            file=audio_file
        )
    return translation.text

# Função para salvar transcrição e tradução em um arquivo Word (.docx)
def export_to_docx(transcription_text, translation_text, output_path="transcription_and_translation.docx"):
    doc = Document()

    doc.add_heading('Transcrição no idioma original:', level=1)
    doc.add_paragraph(transcription_text)

    doc.add_heading('Tradução para o inglês:', level=1)
    doc.add_paragraph(translation_text)

    doc.save(output_path)
    console.print(f"[green]Arquivo salvo com sucesso em: {output_path}[/green]")

if __name__ == "__main__":
    load_dotenv()  # Carrega as variáveis de ambiente do arquivo .env (como a chave da API da OpenAI)

    # Configuração dos argumentos da linha de comando com opções curtas
    parser = argparse.ArgumentParser(description="Transformar texto em áudio, transcrever e traduzir")
    
    # Opção curta -f para o arquivo de texto de entrada
    parser.add_argument("-f", "--file", type=str, required=True, help="Caminho para o arquivo de texto de entrada")
    
    # Opção curta -o para o arquivo de áudio gerado
    parser.add_argument("-o", "--output_audio", type=str, default="output_audio.mp3", help="Caminho para o arquivo de áudio gerado")
    
    # Opção curta -d para o arquivo .docx gerado
    parser.add_argument("-d", "--output_docx", type=str, default="transcription_and_translation.docx", help="Nome do arquivo de saída .docx")

    args = parser.parse_args()

    # Passo 1: Ler o arquivo de texto de entrada
    with open(args.file, "r", encoding="utf-8") as f:
        input_text = f.read()

    # Passo 2: Converter texto em áudio usando gTTS
    text_to_speech(input_text, args.output_audio)

    # Passo 3: Transcrever o áudio gerado
    transcription_text = transcribe_audio(args.output_audio)
    console.print(Panel.fit(f"[bold]Transcrição no idioma original:[/bold]\n{transcription_text}",
                            title="Transcrição", subtitle="Idioma Original", border_style="blue"))

    # Passo 4: Traduzir o áudio para inglês
    translation_text = translate_audio(args.output_audio)
    console.print(Panel.fit(f"[bold]Tradução para o inglês:[/bold]\n{translation_text}",
                            title="Tradução", subtitle="EN-US", border_style="green"))

    # Passo 5: Exportar a transcrição e tradução para um arquivo .docx
    export_to_docx(transcription_text, translation_text, args.output_docx)
