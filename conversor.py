import customtkinter as ctk
from settings import *

#------------------ROOT--------------------------------
class App(ctk.CTk):
    def __init__(self):
        
        #Setup
        super().__init__()
        self.title=('Conversor de imagenes')
        self.geometry('500x600')
        self.resizable(False,False)
        
        #Widgets
        OptionsFrame(self)
        TitleFrame(self)
        MainFrame(self)
        
        self.mainloop()
        
class OptionsFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master = parent)
        self.place(x = 0, y = 0, relwidth = 1, relheight = 0.1)
        font = ctk.CTkFont(family=FONT, size=TITLE_TEXT_SIZE)
        
        #Buttons
        conversor_button = ctk.CTkButton(self, text = 'Conversor', font = font, text_color=BLACK, fg_color=LIGHT_GRAY, hover_color=GRAY)
        conversor_button.pack(side = 'left', expand = True, fill = 'both')
        
        google_drive_button = ctk.CTkButton(self, text = 'Google Drive', font = font, text_color=BLACK, fg_color=LIGHT_GRAY, hover_color=GRAY)
        google_drive_button.pack(side = 'left', expand = True, fill = 'both')
        

class TitleFrame(ctk.CTkLabel):
    def __init__(self, parent):
        font = ctk.CTkFont(family=FONT, size=25, weight='bold')
        super().__init__(master=parent, text = 'Conversor de Imagenes', font= font, text_color = BLACK)
        self.place(relx=0.24,rely=0.1)
      
class MainFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master = parent, fg_color = GREEN)
        font = ctk.CTkFont(family=FONT, size=25, weight='bold')
        self.place(x=0,rely=0.15, relwidth = 1, relheight = 1)
        
        # Layout
        self.columnconfigure(0, weight=1)
        self.rowconfigure((0,1,2,3,4), weight =1, uniform='c')
        
        #Data
        self.path_string = ctk.StringVar()  
        self.path_string.trace_add("write", self.update_path)
        
        #Widgets
        SettingsFrame(self)
        StringFrame(self, self.path_string)
        ButtonConvert(self)
        ProgressBar(self)
        

        
    def update_path(self, *args):
        path_string = self.path_string.get()
        print("Ruta seleccionada:", path_string)
        
        
class SettingsFrame(ctk.CTkFrame):
    def __init__(self, parent):
        font = ctk.CTkFont(family=FONT, size=25, weight='bold')
        super().__init__(master = parent, fg_color=GREEN)
        self.grid(row= 0, column=0, rowspan=2, sticky = 'nsew')
        
        #Variables 
        self.path_string = ctk.StringVar()
        
        # Layout
        self.columnconfigure((0,1,2,3,4,5), weight=1)
        self.rowconfigure((0,1), weight =1, uniform='d')
        
        #Widgets
        
        #--First Row
        path_label = ctk.CTkLabel(self, text = 'Ruta:', font = font, text_color = BLACK)
        path_label.grid(row=0, column=0,sticky = 'nsew')
        
        path_entry = ctk.CTkEntry(master=self,
                               placeholder_text="Ruta de la carpeta",
                               text_color=BLACK,
                               placeholder_text_color =GREEN,
                               width=250,
                               height=25,
                               state='disabled',
                               fg_color=GRAY,
                               textvariable = self.path_string)
        path_entry.grid(row = 0, column=1, columnspan=2, sticky = 'ew')
        
        path_button = ctk.CTkButton(self,
                                    text="Buscar",
                                    command= self.browse_path)  
        path_button.grid(row = 0, column = 4)      
        
        #--Second Row
        drive_label = ctk.CTkLabel(self, text = '  Google Drive: ', font = font, text_color = BLACK)
        drive_label.grid(row=1, column=0,sticky = 'nsew')
        
        path_button = ctk.CTkCheckBox(self,
                                    text="Activar Drive")  
        path_button.grid(row = 1, column = 2, sticky = 'nsew')   
        
        
    #--FUNCTIONS
    def browse_path(self):
        folder_path = ctk.filedialog.askdirectory(
            title="Seleccionar carpeta")
        self.path_string.set(folder_path)
        self.master.path_string.set(folder_path)
        
        
        
class StringFrame(ctk.CTkFrame):
    def __init__(self, parent, path):
        font = ctk.CTkFont(family=FONT, size=30, weight='bold')
        super().__init__(master = parent, fg_color=DARK_GREEN)
        self.grid(row= 2, column=0, sticky = 'nsew')
        
        #variables
        if path != "/PY_VAR0":
            cant = 0
        else: 
            cant = 1
        
        #Widgets
        cant_label = ctk.CTkLabel(self, text = f'Se han encontrado ..{path}', font = font, text_color = BLACK)
        cant_label.pack()
        ext_label = ctk.CTkLabel(self, text = 'Fotos tipo', font = font, text_color = BLACK)
        ext_label.pack()
        
class ButtonConvert(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master = parent,fg_color=TURQUOISE_GREEN)
        self.grid(row= 3, column=0, sticky = 'nsew')
        
        #Widgets
        convert = ctk.CTkButton(self,
                                text="Convertir Fotos")  
        convert.pack(pady=45)
        
class ProgressBar(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master = parent, fg_color= MINT_GREEN )
        self.grid(row= 4, column=0, sticky = 'nsew')
        
        #Widgets
        progress_bar = ctk.CTkProgressBar(self, width=400)
        progress_bar.pack(pady=10)


if __name__ == '__main__':
    App()
        
        