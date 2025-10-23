import customtkinter as ctk
from pdf2image import convert_from_path
from PIL import Image, ImageTk
from pathlib import Path

def mostrar_libro():
    app = ctk.CTk()
    app.geometry("1280x720")
    app.title("Visor de PDF")
    
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")
    
    def handle_button():
        pdf_file = Path(__file__).parent.parent / "data" / "libro.pdf"
        
        if not pdf_file.exists():
            print(f"Error: No se encuentra el archivo en {pdf_file}")
            return
        
        print(f"Abriendo PDF desde: {pdf_file}")
        
        # Ocultar el botón
        abrir.pack_forget()
        
        try:
            # Convertir PDF a imágenes
            print("Convirtiendo PDF...")
            images = convert_from_path(str(pdf_file), dpi=100)
            print(f"Total de páginas: {len(images)}")
            
            # Crear scrollable frame
            scrollable = ctk.CTkScrollableFrame(app, fg_color="#2b2b2b")
            scrollable.pack(fill="both", expand=True, padx=10, pady=10)
            
            # Lista para mantener referencias
            photos = []
            
            # Procesar y mostrar cada página
            for i, img in enumerate(images):
                print(f"Procesando página {i+1}/{len(images)}...")
                
                # Redimensionar
                max_width = 1200
                if img.width > max_width:
                    ratio = max_width / img.width
                    new_size = (max_width, int(img.height * ratio))
                    img = img.resize(new_size, Image.Resampling.LANCZOS)
                
                # Convertir para Tkinter
                photo = ImageTk.PhotoImage(img)
                photos.append(photo)
                
                # Crear label con la imagen usando CTkLabel
                lbl = ctk.CTkLabel(scrollable, image=photo, text="")
                lbl.image = photo  # Mantener referencia
                lbl.pack(pady=10)
            
            print("PDF cargado exitosamente!")
            
        except Exception as e:
            print(f"Error al cargar PDF: {e}")
            import traceback
            traceback.print_exc()
    
    # Botón
    abrir = ctk.CTkButton(app, text="Abrir PDF", command=handle_button, width=200, height=40)
    abrir.pack(expand=True)
    
    app.mainloop()
