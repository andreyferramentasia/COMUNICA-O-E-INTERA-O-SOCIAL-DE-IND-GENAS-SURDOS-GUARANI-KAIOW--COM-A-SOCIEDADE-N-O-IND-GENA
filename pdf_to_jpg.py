import os
from pdf2image import convert_from_path

# pasta com PDFs
input_folder = r"C:\Users\Andrey\Desktop\COMUNICAÇÃO-E-INTERAÇÃO-SOCIAL-DE-INDÍGENAS-SURDOS-GUARANI-KAIOWÁ-COM-A-SOCIEDADE-NÃO-INDÍGENA\pdfs_imagens"

# pasta de saída
output_folder = r"C:\Users\Andrey\Desktop\COMUNICAÇÃO-E-INTERAÇÃO-SOCIAL-DE-INDÍGENAS-SURDOS-GUARANI-KAIOWÁ-COM-A-SOCIEDADE-NÃO-INDÍGENA\imagens"

# caminho do poppler (Windows)
poppler_path = r"C:\Users\Andrey\Desktop\COMUNICAÇÃO-E-INTERAÇÃO-SOCIAL-DE-INDÍGENAS-SURDOS-GUARANI-KAIOWÁ-COM-A-SOCIEDADE-NÃO-INDÍGENA\Release-25.12.0-0\poppler-25.12.0\Library\bin"

for file in os.listdir(input_folder):
    if file.lower().endswith(".pdf"):
        pdf_path = os.path.join(input_folder, file)
        pdf_name = os.path.splitext(file)[0]

        # pasta de saída por PDF (mesmo nome do arquivo)
        # prefixo \\?\ para contornar limite de 260 chars do Windows
        pdf_output_folder = "\\\\?\\" + os.path.join(output_folder, pdf_name)
        os.makedirs(pdf_output_folder, exist_ok=True)

        # converte PDF para imagens
        images = convert_from_path(
            pdf_path,
            dpi=300,
            poppler_path=poppler_path
        )

        # salva cada página como JPG
        for i, img in enumerate(images):
            output_name = f"{pdf_name}_page_{i+1}.jpg"
            output_path = os.path.join(pdf_output_folder, output_name)

            img.save(output_path, "JPEG")

        print(f"Convertido: {file} ({len(images)} páginas)")