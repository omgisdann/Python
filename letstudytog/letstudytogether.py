import tkinter as tk
import webbrowser

class Programa:
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.title("LETSTUDYTOGETHER")
        self.janela.geometry("800x225")

    def cabecalho(self):
        self.frame_cabecalho = tk.Frame(self.janela)
        self.frame_cabecalho.place(x=0, y=0, width=800, height=100)
        canvas = tk.Canvas(self.frame_cabecalho, width=800, height=100, bg="lawn green")
        canvas.pack()
        canvas.create_text(400, 50, text="LET STUDY TOGETHER", font=("Arial", 32))
        
    def corpo(self):
        self.frame_corpo = tk.Frame(self.janela, bg="white")
        self.frame_corpo.place(x=0, y=100, width=1000, height=600)

        self.botao_python = tk.Button(self.frame_corpo, text= 'Aprender Python', command=self.funcionalidade_py)
        self.botao_python.place(x=0, y=5)

        self.botao_java = tk.Button(self.frame_corpo, text='Aprender Java', command=self.funcionalidade_java)
        self.botao_java.place(x=0, y=35)

        self.botao_js = tk.Button(self.frame_corpo, text='Aprender JavaScript', command=self.funcionalidade_js)
        self.botao_js.place(x=0, y=65)

        self.botao_C = tk.Button(self.frame_corpo, text='Aprender C', command=self.funcionalidade_C)
        self.botao_C.place(x=0, y=95)

        self.botao_assembly = tk.Button(self.frame_corpo, text='Aprender Assembly', command=self.funcionalidade_assembly)
        self.botao_assembly.place(x=200, y=5)

        self.botao_csharp = tk.Button(self.frame_corpo, text='Aprender C#', command=self.funcionalidade_csharp)
        self.botao_csharp.place(x=200, y=37)

        self.botao_sql = tk.Button(self.frame_corpo, text='Aprender SQL', command=self.funcionalidade_sql)
        self.botao_sql.place(x=200, y=67)

        self.botao_Cmaismais = tk.Button(self.frame_corpo, text='Aprender C++', command=self.funcionalidade_cmaismais)
        self.botao_Cmaismais.place(x=200, y=96)

        self.botao_TypeScript = tk.Button(self.frame_corpo, text='Aprender TypeScript', command=self.funcionalidade_typescript)
        self.botao_TypeScript.place(x=400, y=5)

        self.botao_php = tk.Button(self.frame_corpo, text='Aprender PHP', command=self.funcionalidade_php)
        self.botao_php.place(x=400, y=37)

        self.botao_go = tk.Button(self.frame_corpo, text='Aprender GoLang', command=self.funcionalidade_go)
        self.botao_go.place(x=400, y=67)

        self.rust = tk.Button(self.frame_corpo, text='Aprender Rust', command=self.funcionalidade_rust)
        self.rust.place(x=400, y=96)

        self.swift = tk.Button(self.frame_corpo, text='Aprender Swift', command=self.funcionalidade_swift)
        self.swift.place(x=600, y=5)

        self.kotlin = tk.Button(self.frame_corpo, text='Aprender Kotlin', command=self.funcionalidade_kotlin)
        self.kotlin.place(x=600, y=37)

        self.dotnet = tk.Button(self.frame_corpo, text='Aprender Visual Basic.Net', command=self.funcionalidade_dotnet)
        self.dotnet.place(x=600, y=67)

        self.ruby =  tk.Button(self.frame_corpo, text='Aprender Ruby', command=self.funcionalidade_ruby)
        self.ruby.place(x=600, y=96)
    def funcionalidade_py(self):
        nova = tk.Toplevel(self.janela)
        nova.title("Aprenda Python")
        nova.geometry("600x200")
        primeiro = tk.Label(nova, text="Canais do Youtube:")
        primeiro.place(x=0, y=0)

        link_guanabara = tk.Button(nova, background="#4946E2",text="Professor Guanabara", command=lambda: webbrowser.open('https://www.youtube.com/@cursoemvideo'))
        link_guanabara.place(x=0, y=20)

        link_hashtag = tk.Button(nova, background="#4946E2",text="HashTag Treinamentos", command=lambda: webbrowser.open('https://www.youtube.com/c/HashtagTreinamentos/videos'))
        link_hashtag.place(x=0, y=50)

        link_dunossauro = tk.Button(nova, background="#4946E2",text="Dunossauro", command=lambda: webbrowser.open('https://www.youtube.com/@Dunossauro'))
        link_dunossauro.place(x=0, y=80)

        link_otavio = tk.Button(nova, background="#4946E2",text="Otávio Miranda", command=lambda: webbrowser.open('https://www.youtube.com/@OtavioMiranda'))
        link_otavio.place(x=0, y=110)

        link_boson = tk.Button(nova, background="#4946E2",text="Boson Treinamentos", command=lambda: webbrowser.open('https://www.youtube.com/@bosontreinamentos'))
        link_boson.place(x=0, y=140)

        segundo = tk.Label(nova, text='Artigos/Sites:')
        segundo.place(x=520, y=0)

        link_udemy = tk.Button(nova, background="#D2E415",text="Udemy", command=lambda: webbrowser.open('https://www.udemy.com/pt/'))
        link_udemy.place(x=550, y=20)

        link_exercism = tk.Button(nova, background="#D2E415",text="Exercism", command=lambda: webbrowser.open('https://exercism.org/pt-BR'))
        link_exercism.place(x=542, y=50)

        link_codeacademy = tk.Button(nova, background="#D2E415",text="Code Academy", command=lambda: webbrowser.open('https://www.codecademy.com/learn/welcome-to-codecademy'))
        link_codeacademy.place(x=507, y=80)

        linkLearnPython = tk.Button(nova, background="#D2E415",text="Learn Python.org", command=lambda: webbrowser.open('https://learnpython.org/'))
        linkLearnPython.place(x=497, y=110)
        
        link_freecodecamp = tk.Button(nova, background="#D2E415",text="FreeCodeCamp", command=lambda: webbrowser.open('https://www.freecodecamp.org/'))
        link_freecodecamp.place(x=506, y=140)

        mensagem_traducao = tk.Label(nova,foreground="#C80606", text='Atenção, caso a página esteja em Inglês, use o traduzir automatico do Google.')
        mensagem_traducao.place(x=0, y=180)
        
    
    def funcionalidade_java(self):
        nova = tk.Toplevel(self.janela)
        nova.title("Aprenda Java")
        nova.geometry("600x200")
        primeiro = tk.Label(nova, text="Canais do Youtube:")
        primeiro.place(x=0, y=0)

        link_guanabara = tk.Button(nova, background="#4946E2",text="Professor Guanabara", command=lambda: webbrowser.open('https://www.youtube.com/@cursoemvideo'))
        link_guanabara.place(x=0, y=20)
        
        link_loiane= tk.Button(nova, background="#4946E2",text="Loiane Groner", command=lambda: webbrowser.open('https://www.youtube.com/watch?v=LnORjqZUMIQ&t=1s'))
        link_loiane.place(x=0, y=50)
        
        link_dev_dojo = tk.Button(nova, background="#4946E2",text="Dev Dojo", command=lambda: webbrowser.open('https://www.youtube.com/@DevDojoBrasil'))
        link_dev_dojo.place(x=0, y=80)
        
        link_FernandaKipper = tk.Button(nova, background="#4946E2",text="Fernanda Kipper", command=lambda: webbrowser.open('https://www.youtube.com/@kipperdev'))
        link_FernandaKipper.place(x=0, y=110)
        
        link_academiadosdev = tk.Button(nova, background="#4946E2",text="Academia dos Dev", command=lambda: webbrowser.open('https://www.youtube.com/@AcademiadosDevs'))
        link_academiadosdev.place(x=0, y=140)

        segundo = tk.Label(nova, text='Artigos/Sites:')
        segundo.place(x=520, y=0)
    
        link_udemy = tk.Button(nova, background="#DD0D18",text="Udemy", command=lambda: webbrowser.open('https://www.udemy.com/pt/'))
        link_udemy.place(x=550, y=20)
    
        link_programiz = tk.Button(nova, background="#DD0D18",text="Programiz", command=lambda: webbrowser.open('https://www.programiz.com/'))
        link_programiz.place(x=535, y=50)
    
        link_devjava = tk.Button(nova, background="#DD0D18",text="Dev Java", command=lambda: webbrowser.open('https://dev.java/'))
        link_devjava.place(x=543, y=80)
    
        linkw3school = tk.Button(nova, background="#DD0D18",text="W3 Schools", command=lambda: webbrowser.open('https://www.w3schools.com/'))
        linkw3school.place(x=527, y=110)
            
        link_freecodecamp = tk.Button(nova, background="#DD0D18",text="FreeCodeCamp", command=lambda: webbrowser.open('https://www.freecodecamp.org/'))
        link_freecodecamp.place(x=506, y=140)

        mensagem_traducao = tk.Label(nova,foreground="#C80606", text='Atenção, caso a página esteja em Inglês, use o traduzir automatico do Google.')
        mensagem_traducao.place(x=0, y=180)


    def funcionalidade_js(self):
        nova = tk.Toplevel(self.janela)
        nova.title("Aprenda JavaScript")
        nova.geometry("600x200")
        primeiro = tk.Label(nova, text="Canais do Youtube:")
        primeiro.place(x=0, y=0)

        link_guanabara = tk.Button(nova, background="#D2E415",text="Professor Guanabara", command=lambda: webbrowser.open('https://www.youtube.com/@cursoemvideo'))
        link_guanabara.place(x=0, y=20)
    
        link_mattheusbattisti = tk.Button(nova, background="#D2E415",text="Matheus Battisti", command=lambda: webbrowser.open('https://www.youtube.com/@MatheusBattisti'))
        link_mattheusbattisti.place(x=0, y=50)
    
        link_rafaellaballerini = tk.Button(nova, background="#D2E415",text="Rafaella Ballerini", command=lambda: webbrowser.open('https://www.youtube.com/watch?v=RjfhRZXB_U8&list=PLhkO7OMKgT_rRK3qvJsZAy3jrkupOxD_h'))
        link_rafaellaballerini.place(x=0, y=80)
        
        link_programacaoweb = tk.Button(nova, background="#D2E415",text="ProgramaçãoWeb", command=lambda: webbrowser.open('https://www.youtube.com/@programacaoweb'))
        link_programacaoweb.place(x=0, y=110)
        
        link_CFBCURSOS = tk.Button(nova, background="#D2E415",text="CFB Cursos", command=lambda: webbrowser.open('https://www.youtube.com/@cfbcursos'))
        link_CFBCURSOS.place(x=0, y=140)


        segundo = tk.Label(nova, text='Artigos/Sites:')
        segundo.place(x=520, y=0)
        
        link_udemy = tk.Button(nova, foreground="#FFF6F6", background="#000000",text="Udemy", command=lambda: webbrowser.open('https://www.udemy.com/pt/'))
        link_udemy.place(x=550, y=20)
        
        link_modernjs = tk.Button(nova, foreground="#FFF6F6", background="#000000",text="Modern JavaScript", command=lambda: webbrowser.open('https://javascript.info/'))
        link_modernjs.place(x=491, y=50)
        
        link_Coddytech = tk.Button(nova, foreground="#FFF6F6", background="#000000",text="Coddy Tech", command=lambda: webbrowser.open('https://coddy.tech/landing/pt/javascript'))
        link_Coddytech.place(x=524, y=80)
        
        linkw3school = tk.Button(nova,foreground="#FFF6F6", background="#000000",text="W3 Schools", command=lambda: webbrowser.open('https://www.w3schools.com/'))
        linkw3school.place(x=527, y=110)
                
        link_freecodecamp = tk.Button(nova,foreground="#FFF6F6", background="#000000",text="FreeCodeCamp", command=lambda: webbrowser.open('https://www.freecodecamp.org/'))
        link_freecodecamp.place(x=506, y=140)

        mensagem_traducao = tk.Label(nova,foreground="#C80606", text='Atenção, caso a página esteja em Inglês, use o traduzir automatico do Google.')
        mensagem_traducao.place(x=0, y=180)


    def funcionalidade_C(self):
        nova = tk.Toplevel(self.janela)
        nova.title("Aprenda C")
        nova.geometry("600x200")
        primeiro = tk.Label(nova, text="Canais do Youtube:")
        primeiro.place(x=0, y=0)    


        link_pxtutoriais = tk.Button(nova, background="#4946E2",text="Pixel Tutoriais", command=lambda: webbrowser.open('https://www.youtube.com/watch?v=Wal10kQKwAE'))
        link_pxtutoriais.place(x=0, y=20)

        link_dealunoparaaluno = tk.Button(nova, background="#4946E2",text="De aluno para aluno", command=lambda: webbrowser.open('https://www.youtube.com/@DeAlunoParaAluno'))
        link_dealunoparaaluno.place(x=0, y=50)

        link_programdesc = tk.Button(nova, background="#4946E2",text="Programação Descomplicada", command=lambda: webbrowser.open('https://www.youtube.com/user/progdescomplicada/playlists'))
        link_programdesc.place(x=0, y=80)

        link_ricardo = tk.Button(nova, background="#4946E2",text="Ricardo Antonello", command=lambda: webbrowser.open('https://www.youtube.com/watch?v=cGTFjX0CVZU'))
        link_ricardo.place(x=0, y=110)

        link_ppbinario = tk.Button(nova, background="#4946E2",text="Papo Binário", command=lambda: webbrowser.open('https://www.youtube.com/playlist?list=PLIfZMtpPYFP5qaS2RFQxcNVkmJLGQwyKE'))
        link_ppbinario.place(x=0, y=140)



        segundo = tk.Label(nova, text='Artigos/Sites:')
        segundo.place(x=520, y=0)
        
        link_udemy = tk.Button(nova, text="Udemy", command=lambda: webbrowser.open('https://www.udemy.com/pt/'))
        link_udemy.place(x=550, y=20)
          
        link_programiz = tk.Button(nova, text="Programiz", command=lambda: webbrowser.open('https://www.programiz.com/'))
        link_programiz.place(x=534, y=50)
          
        link_labexio = tk.Button(nova, text="Labex IO", command=lambda: webbrowser.open('https://labex.io/pt/learn/c'))
        link_labexio.place(x=543, y=80)
          
        linkw3school = tk.Button(nova, text="W3 Schools", command=lambda: webbrowser.open('https://www.w3schools.com/'))
        linkw3school.place(x=527, y=110)
                  
        clanglearning = tk.Button(nova, text="C-Lang Learning", command=lambda: webbrowser.open('https://c-lang-learning.com/pt/index.html'))
        clanglearning.place(x=500, y=140)
      
        mensagem_traducao = tk.Label(nova,foreground="#C80606", text='Atenção, caso a página esteja em Inglês, use o traduzir automatico do Google.')
        mensagem_traducao.place(x=0, y=180)
      
        

    def funcionalidade_assembly(self):
        nova = tk.Toplevel(self.janela)
        nova.title("Aprenda Assembly")
        nova.geometry("600x200")
        primeiro = tk.Label(nova, text="Canais do Youtube:")
        primeiro.place(x=0, y=0)   

        linkblau_araujo = tk.Button(nova, background="#9AA9C1",text="Blau Araujo", command=lambda: webbrowser.open('https://www.youtube.com/@debxp'))
        linkblau_araujo.place(x=0, y=20)

        link_coders = tk.Button(nova, background="#9AA9C1",text="Coders, Assemble!", command=lambda: webbrowser.open('https://www.youtube.com/watch?v=SItcC5j5KGo'))
        link_coders.place(x=0, y=50)

        link_fernandoanselmo = tk.Button(nova, background="#9AA9C1",text="Fernando Anselmo", command=lambda: webbrowser.open('https://www.youtube.com/watch?v=0lfikxs967c&list=PLxTkH01AauxRm0LFLlOA9RR5O6hBLqBtC'))
        link_fernandoanselmo.place(x=0, y=80)

        Pedro_Botelho = tk.Button(nova, background="#9AA9C1",text="Pedro Botelho", command=lambda: webbrowser.open('https://www.youtube.com/watch?v=oMvAPCbBi6s&list=PLSe9457zOLtxKIunClgzm9kqJYg67M5Cw'))
        Pedro_Botelho.place(x=0, y=110)

        link_manualdocodigo = tk.Button(nova, background="#9AA9C1",text="Manual do código", command=lambda: webbrowser.open('https://www.youtube.com/watch?v=WoOVbPnpyjk&list=PLLFRf_pkM7b6Vi0ehPPovl1gQ5ubHTy5P'))
        link_manualdocodigo.place(x=0, y=140)

    
        segundo = tk.Label(nova, text='Artigos/Sites:')
        segundo.place(x=520, y=0)
        
        link_udemy = tk.Button(nova, text="Udemy", background="#C0C0C0" , command=lambda: webbrowser.open('https://www.udemy.com/pt/'))
        link_udemy.place(x=550, y=20)
          
        link_nasm = tk.Button(nova, text="Nasm Tutorial",background="#C0C0C0" ,command=lambda: webbrowser.open('https://cs.lmu.edu/~ray/notes/nasmtutorial/?utm_source=chatgpt.com'))
        link_nasm.place(x=513, y=50)
          
        link_exercism = tk.Button(nova, background="#C0C0C0",text="Exercism", command=lambda: webbrowser.open('https://exercism.org/pt-BR'))
        link_exercism.place(x=542, y=80)
          
        link_mentebinaria = tk.Button(nova, text="Mente Binária", background="#C0C0C0" , command=lambda: webbrowser.open('https://mentebinaria.gitbook.io/assembly?utm_source=chatgpt.com'))
        link_mentebinaria.place(x=515, y=110)
                  
        eletronics_reference = tk.Button(nova, text="Eletronics Reference", background="#C0C0C0" , command=lambda: webbrowser.open('https://electronicsreference.com/assembly-language/?utm_source=chatgpt.com'))
        eletronics_reference.place(x=482, y=140)
      
        mensagem_traducao = tk.Label(nova,foreground="#C80606", text='Atenção, caso a página esteja em Inglês, use o traduzir automatico do Google.')
        mensagem_traducao.place(x=0, y=180)



    def funcionalidade_csharp(self):
        nova = tk.Toplevel(self.janela)
        nova.title("Aprenda C#")
        nova.geometry("600x200")
        primeiro = tk.Label(nova, text="Canais do Youtube:")
        primeiro.place(x=0, y=0)   

        link_balta = tk.Button(nova, background="#7640A8",text="Balta.IO", command=lambda: webbrowser.open('https://www.youtube.com/@baltaio'))
        link_balta.place(x=0, y=20)

        link_fredi = tk.Button(nova, background="#7640A8",text="Fredi!", command=lambda: webbrowser.open('https://www.youtube.com/watch?v=oTivhgjbhIg'))
        link_fredi.place(x=0, y=50)

        link_macoratti = tk.Button(nova, background="#7640A8",text="Macoratti", command=lambda: webbrowser.open('https://www.youtube.com/@josecarlosmacoratti'))
        link_macoratti.place(x=0, y=80)

        link_excript = tk.Button(nova, background="#7640A8",text="eXcript", command=lambda: webbrowser.open('https://www.youtube.com/watch?v=9Uh0ynDB6ko&list=PLesCEcYj003SFffgnOcITHnCJavMf0ArD'))
        link_excript.place(x=0, y=110)

        link_cfbcursos = tk.Button(nova, background="#7640A8",text="CFB cursos", command=lambda: webbrowser.open('https://www.youtube.com/watch?v=dVzJ3bx68FA&list=PLx4x_zx8csUglgKTmgfVFEhWWBQCasNGi'))
        link_cfbcursos.place(x=0, y=140)

    
        segundo = tk.Label(nova, text='Artigos/Sites:')
        segundo.place(x=520, y=0)
        
        link_udemy = tk.Button(nova, text="Udemy", background="#FFFFFF" , command=lambda: webbrowser.open('https://www.udemy.com/pt/'))
        link_udemy.place(x=550, y=20)
            
        link_microsoftlearn = tk.Button(nova, text="Microsoft Learn",background="#FFFFFF" ,command=lambda: webbrowser.open('https://learn.microsoft.com/pt-br/dotnet/csharp/?utm_source=chatgpt.com'))
        link_microsoftlearn.place(x=505, y=50)
            
        link_NET = tk.Button(nova, background="#FFFFFF",text=".NET - Aprenda C#", command=lambda: webbrowser.open('https://dotnet.microsoft.com/pt-br/learn/csharp?utm_source=chatgpt.com'))
        link_NET.place(x=489, y=80)
            
        link_freecodecamp = tk.Button(nova, background="#FFFFFF",text="FreeCodeCamp", command=lambda: webbrowser.open('https://www.freecodecamp.org/'))
        link_freecodecamp.place(x=506, y=110)
                    
        link_exercism = tk.Button(nova, background="#FFFFFF",text="Exercism", command=lambda: webbrowser.open('https://exercism.org/pt-BR'))
        link_exercism.place(x=542, y=140)
        
        mensagem_traducao = tk.Label(nova,foreground="#C80606", text='Atenção, caso a página esteja em Inglês, use o traduzir automatico do Google.')
        mensagem_traducao.place(x=0, y=180)




    def funcionalidade_sql(self):
        nova = tk.Toplevel(self.janela)
        nova.title("Aprenda SQL")
        nova.geometry("600x200")
        primeiro = tk.Label(nova, text="Canais do Youtube:")
        primeiro.place(x=0, y=0)

        link_guanabara = tk.Button(nova, background="#4946E2",text="Professor Guanabara", command=lambda: webbrowser.open('https://www.youtube.com/@cursoemvideo'))
        link_guanabara.place(x=0, y=20)

        link_hashtag = tk.Button(nova, background="#4946E2",text="HashTag Treinamentos", command=lambda: webbrowser.open('https://www.youtube.com/c/HashtagTreinamentos/videos'))
        link_hashtag.place(x=0, y=50)

        link_ale = tk.Button(nova, background="#4946E2",text="Alessandro Tovato", command=lambda: webbrowser.open('https://www.youtube.com/results?search_query=Alessandro+Trovato+curso+SQL+Server&utm_source=chatgpt.com'))
        link_ale.place(x=0, y=80)

        link_otavio = tk.Button(nova, background="#4946E2",text="Otávio Miranda", command=lambda: webbrowser.open('https://www.youtube.com/@OtavioMiranda'))
        link_otavio.place(x=0, y=110)

        link_boson = tk.Button(nova, background="#4946E2",text="Boson Treinamentos", command=lambda: webbrowser.open('https://www.youtube.com/@bosontreinamentos'))
        link_boson.place(x=0, y=140)

        segundo = tk.Label(nova, text='Artigos/Sites:')
        segundo.place(x=520, y=0)

        link_udemy = tk.Button(nova, background="#FFFFFF",text="Udemy", command=lambda: webbrowser.open('https://www.udemy.com/pt/'))
        link_udemy.place(x=550, y=20)

        link_sqlzoo = tk.Button(nova, background="#FFFFFF",text="Sql Zoo", command=lambda: webbrowser.open('https://sqlzoo.net/wiki/SQL_Tutorial?utm_source=chatgpt.com'))
        link_sqlzoo.place(x=548, y=50)

        link_codeacademy = tk.Button(nova, background="#FFFFFF",text="Code Academy", command=lambda: webbrowser.open('https://www.codecademy.com/learn/welcome-to-codecademy'))
        link_codeacademy.place(x=507, y=80)
    
        linkw3school = tk.Button(nova, background="#FFFFFF", text="W3 Schools", command=lambda: webbrowser.open('https://www.w3schools.com/'))
        linkw3school.place(x=527, y=110)
        
        link_freecodecamp = tk.Button(nova, background="#FFFFFF",text="FreeCodeCamp", command=lambda: webbrowser.open('https://www.freecodecamp.org/'))
        link_freecodecamp.place(x=506, y=140)

        mensagem_traducao = tk.Label(nova,foreground="#C80606", text='Atenção, caso a página esteja em Inglês, use o traduzir automatico do Google.')
        mensagem_traducao.place(x=0, y=180)



    def funcionalidade_cmaismais(self):
        nova = tk.Toplevel(self.janela)
        nova.title("Aprenda C++")
        nova.geometry("600x200")
        primeiro = tk.Label(nova, text="Canais do Youtube:")
        primeiro.place(x=0, y=0)

        link_excript = tk.Button(nova, background="#4946E2", text="eXcript", command=lambda: webbrowser.open('https://www.youtube.com/results?search_query=eXcript+curso+C%2B%2B&utm_source=chatgpt.com'))
        link_excript.place(x=0, y=20)

        link_alandefreitas = tk.Button(nova, background="#4946E2",text="Alan De Freitas", command=lambda: webbrowser.open('https://www.youtube.com/playlist?list=PLIUc9-A-aPpqrzY3YuWDUOyQLOBCb5lck&utm_source=chatgpt.com'))
        link_alandefreitas.place(x=0, y=50)

        link_castro = tk.Button(nova, background="#4946E2",text="Marcos Castro", command=lambda: webbrowser.open('https://www.youtube.com/playlist?list=PL8eBmR3QtPL13Dkn5eEfmG9TmzPpTp0cV&utm_source=chatgpt.com'))
        link_castro.place(x=0, y=80)

        link_bruno = tk.Button(nova, background="#4946E2",text="Professor Bruno", command=lambda: webbrowser.open('https://www.youtube.com/playlist?list=PLx4x_zx8csUjczg1qPHavU1vw1IkBcm40&utm_source=chatgpt.com'))
        link_bruno.place(x=0, y=110)

        link_cfbcursos = tk.Button(nova, background="#4946E2",text="CFB cursos", command=lambda: webbrowser.open('https://www.youtube.com/watch?v=dVzJ3bx68FA&list=PLx4x_zx8csUglgKTmgfVFEhWWBQCasNGi'))
        link_cfbcursos.place(x=0, y=140)

        segundo = tk.Label(nova, text='Artigos/Sites:')
        segundo.place(x=520, y=0)

        link_udemy = tk.Button(nova, background="#FFFFFF",text="Udemy", command=lambda: webbrowser.open('https://www.udemy.com/pt/'))
        link_udemy.place(x=550, y=20)

        microsoft_learn = tk.Button(nova, background="#FFFFFF",text="Microsoft Learn", command=lambda: webbrowser.open('https://learn.microsoft.com/pt-br/cpp/cpp/?utm_source=chatgpt.com'))
        microsoft_learn.place(x=505, y=50)

        cmaismais_br = tk.Button(nova, background="#FFFFFF",text="C++ Brasil", command=lambda: webbrowser.open('https://github.com/cppbrasil/material-de-aprendizado?utm_source=chatgpt.com'))
        cmaismais_br.place(x=533 ,y=80)

        linkw3school = tk.Button(nova, background="#FFFFFF", text="W3 Schools", command=lambda: webbrowser.open('https://www.w3schools.com/'))
        linkw3school.place(x=527, y=110)
        
        LearnCpp = tk.Button(nova, background="#FFFFFF",text="Learn Cpp", command=lambda: webbrowser.open('https://www.learncpp.com/?utm_source=chatgpt.com'))
        LearnCpp.place(x=533, y=140)

        mensagem_traducao = tk.Label(nova,foreground="#C80606", text='Atenção, caso a página esteja em Inglês, use o traduzir automatico do Google.')
        mensagem_traducao.place(x=0, y=180)




    def funcionalidade_typescript(self):
        nova = tk.Toplevel(self.janela)
        nova.title("Aprenda TypeScript")
        nova.geometry("600x200")
        primeiro = tk.Label(nova, text="Canais do Youtube:")
        primeiro.place(x=0, y=0)

        link_glaucialemos = tk.Button(nova, background="#3178C6", text="Glaucia Lemos", command=lambda: webbrowser.open('https://www.youtube.com/@GlauciaLemos'))
        link_glaucialemos.place(x=0, y=20)

        link_dev_dojo = tk.Button(nova, background="#3178C6",text="Dev Dojo", command=lambda: webbrowser.open('https://www.youtube.com/@DevDojoBrasil'))
        link_dev_dojo.place(x=0, y=50)

        link_justen = tk.Button(nova, background="#3178C6",text="Willian Justen", command=lambda: webbrowser.open('https://www.youtube.com/results?search_query=Willian+Justen+Mini-curso+TypeScript'))
        link_justen.place(x=0, y=80)

        link_rodrigobranas = tk.Button(nova, background="#3178C6",text="Rodrigo Branas", command=lambda: webbrowser.open('https://www.youtube.com/results?search_query=Rodrigo+Branas+Masterclass+TypeScript&utm_source=chatgpt.com'))
        link_rodrigobranas.place(x=0, y=110)

        link_cfbcursos = tk.Button(nova, background="#3178C6",text="CFB cursos", command=lambda: webbrowser.open('https://www.youtube.com/watch?v=dVzJ3bx68FA&list=PLx4x_zx8csUglgKTmgfVFEhWWBQCasNGi'))
        link_cfbcursos.place(x=0, y=140)

        segundo = tk.Label(nova, text='Artigos/Sites:')
        segundo.place(x=520, y=0)

        link_udemy = tk.Button(nova, background="#FFFFFF",text="Udemy", command=lambda: webbrowser.open('https://www.udemy.com/pt/'))
        link_udemy.place(x=550, y=20)

        scrimba = tk.Button(nova, background="#FFFFFF",text="Scrimba", command=lambda: webbrowser.open('https://scrimba.com/learn/typescript?utm_source=chatgpt.com'))
        scrimba.place(x=545, y=50)

        lts_org = tk.Button(nova, background="#FFFFFF",text="Learning TypeScript ORG", command=lambda: webbrowser.open('https://learningtypescript.org/lessons?utm_source=chatgpt.com'))
        lts_org.place(x=456, y=80)

        link_freecodecamp = tk.Button(nova, background="#FFFFFF",text="FreeCodeCamp", command=lambda: webbrowser.open('https://www.freecodecamp.org/'))
        link_freecodecamp.place(x=506, y=110)
        
        total_ts = tk.Button(nova, background="#FFFFFF",text="Total TS", command=lambda: webbrowser.open('https://www.totaltypescript.com/books/total-typescript-essentials?utm_source=chatgpt.com'))
        total_ts.place(x=545, y=140)

        mensagem_traducao = tk.Label(nova,foreground="#C80606", text='Atenção, caso a página esteja em Inglês, use o traduzir automatico do Google.')
        mensagem_traducao.place(x=0, y=180)   


    def funcionalidade_php(self):
        nova = tk.Toplevel(self.janela)
        nova.title("Aprenda PHP")
        nova.geometry("600x200")
        primeiro = tk.Label(nova, text="Canais do Youtube:")
        primeiro.place(x=0, y=0)

        link_guanabara = tk.Button(nova, background="#777BB4",text="Professor Guanabara", command=lambda: webbrowser.open('https://www.youtube.com/@cursoemvideo'))
        link_guanabara.place(x=0, y=20)

        link_cfbcursos = tk.Button(nova, background="#777BB4",text="CFB cursos", command=lambda: webbrowser.open('https://www.youtube.com/watch?v=dVzJ3bx68FA&list=PLx4x_zx8csUglgKTmgfVFEhWWBQCasNGi'))
        link_cfbcursos.place(x=0, y=50)

        link_nstreinamentos = tk.Button(nova, background="#777BB4",text="Node Studio", command=lambda: webbrowser.open('https://www.youtube.com/results?search_query=Node+Studio+Treinamentos+curso+PHP&utm_source=chatgpt.com'))
        link_nstreinamentos.place(x=0, y=80)

        link_otavio = tk.Button(nova, background="#777BB4",text="Otávio Miranda", command=lambda: webbrowser.open('https://www.youtube.com/@OtavioMiranda'))
        link_otavio.place(x=0, y=110)

        link_boson = tk.Button(nova, background="#777BB4",text="Boson Treinamentos", command=lambda: webbrowser.open('https://www.youtube.com/@bosontreinamentos'))
        link_boson.place(x=0, y=140)

        segundo = tk.Label(nova, text='Artigos/Sites:')
        segundo.place(x=520, y=0)

        link_udemy = tk.Button(nova, background="#FFFFFF",text="Udemy", command=lambda: webbrowser.open('https://www.udemy.com/pt/'))
        link_udemy.place(x=550, y=20)

        link_exercism = tk.Button(nova, background="#FFFFFF",text="Exercism", command=lambda: webbrowser.open('https://exercism.org/pt-BR'))
        link_exercism.place(x=542, y=50)

        link_manual = tk.Button(nova, background="#FFFFFF",text="PHP Manual", command=lambda: webbrowser.open('https://www.php.net/manual/pt_BR/?utm_source=chatgpt.com'))
        link_manual.place(x=522, y=80)

        link_php = tk.Button(nova, background="#FFFFFF",text="PHP.com", command=lambda: webbrowser.open('https://www.php.com.br/?utm_source=chatgpt.com'))
        link_php.place(x=538, y=110)
        
        link_freecodecamp = tk.Button(nova, background="#FFFFFF",text="FreeCodeCamp", command=lambda: webbrowser.open('https://www.freecodecamp.org/'))
        link_freecodecamp.place(x=506, y=140)

        mensagem_traducao = tk.Label(nova,foreground="#C80606", text='Atenção, caso a página esteja em Inglês, use o traduzir automatico do Google.')
        mensagem_traducao.place(x=0, y=180)


    def funcionalidade_go(self):
        nova = tk.Toplevel(self.janela)
        nova.title("Aprenda Golang")
        nova.geometry("600x200")
        primeiro = tk.Label(nova, text="Canais do Youtube:")
        primeiro.place(x=0, y=0)

        aprenda_Go = tk.Button(nova, background="#4946E2",text="Aprenda Go", command=lambda: webbrowser.open('https://www.youtube.com/@AprendaGo?utm_source=chatgpt.com'))
        aprenda_Go.place(x=0, y=20)

        full_cycle = tk.Button(nova, background="#4946E2",text="Full Cycle", command=lambda: webbrowser.open('https://www.youtube.com/@FullCycle?utm_source=chatgpt.com'))
        full_cycle.place(x=0, y=50)

        link_sc = tk.Button(nova, background="#4946E2",text="Stephani Cardoso", command=lambda: webbrowser.open('https://www.youtube.com/results?search_query=Stephanie+Cardoso+Golang+do+Zero&utm_source=chatgpt.com'))
        link_sc.place(x=0, y=80)

        link_hun = tk.Button(nova, background="#4946E2",text="Hun Coding", command=lambda: webbrowser.open('https://www.youtube.com/@HunCoding?utm_source=chatgpt.com'))
        link_hun.place(x=0, y=110)

        link_nbk = tk.Button(nova, background="#4946E2",text="NBK Mundo Tech", command=lambda: webbrowser.open('https://www.youtube.com/results?search_query=NBK+Mundo+Tech+curso+Golang&utm_source=chatgpt.com'))
        link_nbk.place(x=0, y=140)

        segundo = tk.Label(nova, text='Artigos/Sites:')
        segundo.place(x=520, y=0)

        link_udemy = tk.Button(nova, background="#FFFFFF",text="Udemy", command=lambda: webbrowser.open('https://www.udemy.com/pt/'))
        link_udemy.place(x=550, y=20)

        link_gobr = tk.Button(nova, background="#FFFFFF",text="Go Brasil", command=lambda: webbrowser.open('https://golang.com.br/aprenda/?utm_source=chatgpt.com'))
        link_gobr.place(x=542, y=50)

        link_cursogo = tk.Button(nova, background="#FFFFFF",text="Curso GO", command=lambda: webbrowser.open('https://curso.golang.com.br/?utm_source=chatgpt.com'))
        link_cursogo.place(x=537, y=80)

        youcourse = tk.Button(nova, background="#FFFFFF",text="You Course", command=lambda: webbrowser.open('https://www.youcourse.com.br/topic/go-linguagem-de-programacao?utm_source=chatgpt.com'))
        youcourse.place(x=527, y=110)
        
        link_freecodecamp = tk.Button(nova, background="#FFFFFF",text="FreeCodeCamp", command=lambda: webbrowser.open('https://www.freecodecamp.org/'))
        link_freecodecamp.place(x=506, y=140)

        mensagem_traducao = tk.Label(nova,foreground="#C80606", text='Atenção, caso a página esteja em Inglês, use o traduzir automatico do Google.')
        mensagem_traducao.place(x=0, y=180)




    def funcionalidade_rust(self):
        nova = tk.Toplevel(self.janela)
        nova.title("Aprenda rust")
        nova.geometry("600x200")
        primeiro = tk.Label(nova, text="Canais do Youtube:")
        primeiro.place(x=0, y=0)

        aprenda_rust = tk.Button(nova, foreground="#FFF6F6", background="#000000",text="Aprenda Rust", command=lambda: webbrowser.open('https://www.youtube.com/results?search_query=Bruno+Cesar+Rocha+Aprenda+Rust&utm_source=chatgpt.com'))
        aprenda_rust.place(x=0, y=20)

        master_dev = tk.Button(nova, foreground="#FFF6F6", background="#000000" ,text="Master Dev", command=lambda: webbrowser.open('https://www.youtube.com/results?search_query=Master+Dev+Aprendendo+Rust+Language+do+ZERO&utm_source=chatgpt.com'))
        master_dev.place(x=0, y=50)

        ms_reactor = tk.Button(nova, foreground="#FFF6F6", background="#000000" ,text="Microsoft Reactor", command=lambda: webbrowser.open('https://www.youtube.com/results?search_query=Microsoft+Reactor+Programacao+Basica+em+Rust&utm_source=chatgpt.com'))
        ms_reactor.place(x=0, y=80)

        link_as = tk.Button(nova, foreground="#FFF6F6", background="#000000",text="Antonio Souza", command=lambda: webbrowser.open('https://www.youtube.com/watch?v=FCuL3BrVdds&utm_source=chatgpt.com'))
        link_as.place(x=0, y=110)

        link_w3d = tk.Button(nova, foreground="#FFF6F6", background="#000000",text="WEB3DEV", command=lambda: webbrowser.open('https://www.youtube.com/watch?v=7rquZPI5B-k&utm_source=chatgpt.com'))
        link_w3d.place(x=0, y=140)

        segundo = tk.Label(nova, text='Artigos/Sites:')
        segundo.place(x=520, y=0)

        link_udemy = tk.Button(nova, background="#FFFFFF",text="Udemy", command=lambda: webbrowser.open('https://www.udemy.com/pt/'))
        link_udemy.place(x=550, y=20)

        link_ur = tk.Button(nova, background="#FFFFFF",text="Universo Rust", command=lambda: webbrowser.open('https://universorust.com/?utm_source=chatgpt.com'))
        link_ur.place(x=516, y=50)

        link_rustbrasil = tk.Button(nova, background="#FFFFFF",text="Rust BR", command=lambda: webbrowser.open('https://www.rustlang.com.br/aprenda/?utm_source=chatgpt.com'))
        link_rustbrasil.place(x=548, y=80)

        tutorial_rust = tk.Button(nova, background="#FFFFFF",text="Tutorial de Rust", command=lambda: webbrowser.open('https://rusttutorial.org/pt-br/?utm_source=chatgpt.com'))
        tutorial_rust.place(x=505, y=110)
        
        dev_community = tk.Button(nova, background="#FFFFFF",text="Dev Community", command=lambda: webbrowser.open('https://dev.to/gabrielteixeira44/entao-voce-quer-aprender-rust-3ak6?utm_source=chatgpt.com'))
        dev_community.place(x=500, y=140)

        mensagem_traducao = tk.Label(nova,foreground="#C80606", text='Atenção, caso a página esteja em Inglês, use o traduzir automatico do Google.')
        mensagem_traducao.place(x=0, y=180)   



    def funcionalidade_swift(self):
        nova = tk.Toplevel(self.janela)
        nova.title("Aprenda Swift")
        nova.geometry("600x200")
        primeiro = tk.Label(nova, text="Canais do Youtube:")
        primeiro.place(x=0, y=0)

        tiago_aguiar = tk.Button(nova,background="#F05138",text="Tiago Aguiar", command=lambda: webbrowser.open('https://www.youtube.com/results?search_query=Tiago+Aguiar+curso+Swift&utm_source=chatgpt.com'))
        tiago_aguiar.place(x=0, y=20)

        attekita_dev = tk.Button(nova,background="#F05138" ,text="Attekita Dev", command=lambda: webbrowser.open('https://www.youtube.com/results?search_query=Attekita+Dev+Swift&utm_source=chatgpt.com'))
        attekita_dev.place(x=0, y=50)

        codemus = tk.Button(nova,background="#F05138" ,text="Codemus", command=lambda: webbrowser.open('https://www.youtube.com/results?search_query=C%C3%ADcero+Camargo+CODEMUS+Swift&utm_source=chatgpt.com'))
        codemus.place(x=0, y=80)

        cocoaheadsbr = tk.Button(nova,background="#F05138",text="CocoaHeadsBr", command=lambda: webbrowser.open('https://www.youtube.com/results?search_query=CocoaHeads+Brasil+Swift&utm_source=chatgpt.com'))
        cocoaheadsbr.place(x=0, y=110)

        swift_para_todos = tk.Button(nova,background="#F05138",text="Swift para todos", command=lambda: webbrowser.open('https://www.youtube.com/results?search_query=Swift+para+todos+Swift&utm_source=chatgpt.com'))
        swift_para_todos.place(x=0, y=140)

        segundo = tk.Label(nova, text='Artigos/Sites:')
        segundo.place(x=520, y=0)

        link_udemy = tk.Button(nova, background="#FFFFFF",text="Udemy", command=lambda: webbrowser.open('https://www.udemy.com/pt/'))
        link_udemy.place(x=550, y=20)

        codando_apple = tk.Button(nova, background="#FFFFFF",text="Codando Apple", command=lambda: webbrowser.open('https://github.com/CodandoApple/aprenda-swift?utm_source=chatgpt.com'))
        codando_apple.place(x=505, y=50)

        dev_paw = tk.Button(nova, background="#FFFFFF",text="Dev Paw", command=lambda: webbrowser.open('https://www.dev-paw.com/pt-br/?utm_source=chatgpt.com'))
        dev_paw.place(x=543, y=80)

        apple_education = tk.Button(nova, background="#FFFFFF",text="Apple Education", command=lambda: webbrowser.open('https://education.apple.com/learning-center/T021340A-pt_BR?utm_source=chatgpt.com'))
        apple_education.place(x=500, y=110)
        
        mac_magazine = tk.Button(nova, background="#FFFFFF",text="Mac Magazine", command=lambda: webbrowser.open('https://macmagazine.com.br/post/2015/06/24/quaddro-macmagazine-vamos-aprender-swift/?utm_source=chatgpt.com'))
        mac_magazine.place(x=510, y=140)

        mensagem_traducao = tk.Label(nova,foreground="#C80606", text='Atenção, caso a página esteja em Inglês, use o traduzir automatico do Google.')
        mensagem_traducao.place(x=0, y=180)   


    def funcionalidade_kotlin(self):
        nova = tk.Toplevel(self.janela)
        nova.title("Aprenda Kotlin")
        nova.geometry("600x200")
        primeiro = tk.Label(nova, text="Canais do Youtube:")
        primeiro.place(x=0, y=0)

        tiago_aguiar = tk.Button(nova,background="#7F52FF",text="Tiago Aguiar", command=lambda: webbrowser.open('https://www.youtube.com/results?search_query=Tiago+Aguiar+curso+Swift&utm_source=chatgpt.com'))
        tiago_aguiar.place(x=0, y=20)
      
        link_erudio = tk.Button(nova, background="#7F52FF",text="Erudio", command=lambda: webbrowser.open('https://www.youtube.com/c/HashtagTreinamentos/videos'))
        link_erudio.place(x=0, y=50)

        link_android = tk.Button(nova, background="#7F52FF",text="Android", command=lambda: webbrowser.open('https://www.youtube.com/results?search_query=Android+Simples+e+Direto+Kotlin&utm_source=chatgpt.com'))
        link_android.place(x=0, y=80)

        link_rapaduradev = tk.Button(nova, background="#7F52FF",text="Rapadura Dev", command=lambda: webbrowser.open('https://www.youtube.com/results?search_query=Rapadura+Dev+Kotlin&utm_source=chatgpt.com'))
        link_rapaduradev.place(x=0, y=110)

        link_dm = tk.Button(nova, background="#7F52FF",text="Douglas Motta", command=lambda: webbrowser.open('https://www.youtube.com/results?search_query=Douglas+Motta+curso+Kotlin&utm_source=chatgpt.com'))
        link_dm.place(x=0, y=140)

        segundo = tk.Label(nova, text='Artigos/Sites:')
        segundo.place(x=520, y=0)

        link_udemy = tk.Button(nova, background="#F05138",text="Udemy", command=lambda: webbrowser.open('https://www.udemy.com/pt/'))
        link_udemy.place(x=550, y=20)

        kotlin_br = tk.Button(nova, background="#F05138",text="Kotlin BR", command=lambda: webbrowser.open('https://kotlin.dev.br/guias/guia-completo-kotlin/?utm_source=chatgpt.com'))
        kotlin_br.place(x=540, y=50)

        link_androiddev = tk.Button(nova, background="#F05138",text="Android Dev", command=lambda: webbrowser.open('https://developer.android.com/courses/android-development-with-kotlin/unit-1?hl=pt-BR&utm_source=chatgpt.com'))
        link_androiddev.place(x=522, y=80)

        link_Coddy = tk.Button(nova, background="#F05138",text="Coddy", command=lambda: webbrowser.open('https://coddy.tech/landing/pt/kotlin?utm_source=chatgpt.com'))
        link_Coddy.place(x=552, y=110)
        
        jetbrainsacademy = tk.Button(nova, background="#F05138",text="JetBrains", command=lambda: webbrowser.open('https://www.jetbrains.com/pt-br/pages/academy/kotlin/?utm_source=chatgpt.com'))
        jetbrainsacademy.place(x=542, y=140)

        mensagem_traducao = tk.Label(nova,foreground="#C80606", text='Atenção, caso a página esteja em Inglês, use o traduzir automatico do Google.')
        mensagem_traducao.place(x=0, y=180)


    def funcionalidade_dotnet(self):
        nova = tk.Toplevel(self.janela)
        nova.title("Aprenda Visual Basic.NET")
        nova.geometry("600x200")
        primeiro = tk.Label(nova, text="Canais do Youtube:")
        primeiro.place(x=0, y=0)

        jc_macoratti = tk.Button(nova, background="#4946E2",text="José Carlos Macoratti", command=lambda: webbrowser.open('https://www.youtube.com/results?search_query=Jos%C3%A9+Carlos+Macoratti+Visual+Basic+NET&utm_source=chatgpt.com'))
        jc_macoratti.place(x=0, y=20)

        link_marciofessini = tk.Button(nova, background="#4946E2",text="Marcio Fessini", command=lambda: webbrowser.open('https://www.youtube.com/watch?v=yaOlNxorIWA&utm_source=chatgpt.com'))
        link_marciofessini.place(x=0, y=50)

        otavinomota = tk.Button(nova, background="#4946E2",text="Otavino Mota", command=lambda: webbrowser.open('https://www.youtube.com/watch?v=CMhCNyQsYeg&utm_source=chatgpt.com'))
        otavinomota.place(x=0, y=80)

        link_dotnet = tk.Button(nova, background="#4946E2",text="Canal .NET", command=lambda: webbrowser.open('https://www.youtube.com/@CanalDotNET?utm_source=chatgpt.com'))
        link_dotnet.place(x=0, y=110)

        link_boson = tk.Button(nova, background="#4946E2",text="Boson Treinamentos", command=lambda: webbrowser.open('https://www.youtube.com/@bosontreinamentos'))
        link_boson.place(x=0, y=140)

        segundo = tk.Label(nova, text='Artigos/Sites:')
        segundo.place(x=520, y=0)

        link_udemy = tk.Button(nova, background="#FFFFFF",text="Udemy", command=lambda: webbrowser.open('https://www.udemy.com/pt/'))
        link_udemy.place(x=550, y=20)

        link_mslearn = tk.Button(nova, background="#FFFFFF",text="Ms Learn", command=lambda: webbrowser.open('https://learn.microsoft.com/pt-br/dotnet/visual-basic/?utm_source=chatgpt.com'))
        link_mslearn.place(x=540, y=50)

        link_juliobattisti = tk.Button(nova, background="#FFFFFF",text="Julio Battisti", command=lambda: webbrowser.open('https://juliobattisti.com.br/tutoriais/lista-categorias.asp?utm_source=chatgpt.com'))
        link_juliobattisti.place(x=525, y=80)
    
        link_ttpoint = tk.Button(nova, background="#FFFFFF", text="Tutorials Point", command=lambda: webbrowser.open('https://www.tutorialspoint.com/vb.net/index.htm?utm_source=chatgpt.com'))
        link_ttpoint.place(x=511, y=110)
        
        link_exercism = tk.Button(nova, background="#FFFFFF",text="Exercism", command=lambda: webbrowser.open('https://exercism.org/pt-BR'))
        link_exercism.place(x=542, y=140)

        mensagem_traducao = tk.Label(nova,foreground="#C80606", text='Atenção, caso a página esteja em Inglês, use o traduzir automatico do Google.')
        mensagem_traducao.place(x=0, y=180)



    def funcionalidade_ruby(self):
        nova = tk.Toplevel(self.janela)
        nova.title("Aprenda Ruby")
        nova.geometry("600x200")
        primeiro = tk.Label(nova, text="Canais do Youtube:")
        primeiro.place(x=0, y=0)

        puts_dev = tk.Button(nova,background="#FF0000",text="Puts Dev", command=lambda: webbrowser.open('https://www.youtube.com/results?search_query=Puts+Dev+Ruby&utm_source=chatgpt.com'))
        puts_dev.place(x=0, y=20)

        onebitcode = tk.Button(nova,background="#FF0000" ,text="OneBitCode", command=lambda: webbrowser.open('https://www.youtube.com/results?search_query=OneBitCode+curso+Ruby&utm_source=chatgpt.com'))
        onebitcode.place(x=0, y=50)

        lucas_caton = tk.Button(nova,background="#FF0000" ,text="Lucas Caton", command=lambda: webbrowser.open('https://www.youtube.com/results?search_query=Lucas+Caton+Ruby+on+Rails&utm_source=chatgpt.com'))
        lucas_caton.place(x=0, y=80)

        noobcode = tk.Button(nova,background="#FF0000",text="NoobCode", command=lambda: webbrowser.open('https://www.youcourse.com.br/course/curso-de-ruby-para-iniciantes?utm_source=chatgpt.com'))
        noobcode.place(x=0, y=110)

        link_boson = tk.Button(nova, background="#FF0000",text="Boson Treinamentos", command=lambda: webbrowser.open('https://www.youtube.com/@bosontreinamentos'))
        link_boson.place(x=0, y=140)

        segundo = tk.Label(nova, text='Artigos/Sites:')
        segundo.place(x=520, y=0)

        link_udemy = tk.Button(nova, background="#FFFFFF",text="Udemy", command=lambda: webbrowser.open('https://www.udemy.com/pt/'))
        link_udemy.place(x=550, y=20)

        ruby_docoficial = tk.Button(nova, background="#FFFFFF",text="Ruby Doc Oficial", command=lambda: webbrowser.open('https://www.ruby-lang.org/pt/documentation/?utm_source=chatgpt.com'))
        ruby_docoficial.place(x=500, y=50)

        rubyemvintemin = tk.Button(nova, background="#FFFFFF",text="Ruby em vinte minutos", command=lambda: webbrowser.open('https://www.ruby-lang.org/pt/documentation/quickstart/?utm_source=chatgpt.com'))
        rubyemvintemin.place(x=465, y=80)

        rubyonrailsbr = tk.Button(nova, background="#FFFFFF",text="Ruby On Rails BR", command=lambda: webbrowser.open('https://rubyonrailsbrasil.com.br/iniciantes/?utm_source=chatgpt.com'))
        rubyonrailsbr.place(x=498, y=110)
        
        oguia = tk.Button(nova, background="#FFFFFF",text="O guia de Ruby", command=lambda: webbrowser.open('https://why.carlosbrando.com/?utm_source=chatgpt.com'))
        oguia.place(x=507, y=140)

        mensagem_traducao = tk.Label(nova,foreground="#C80606", text='Atenção, caso a página esteja em Inglês, use o traduzir automatico do Google.')
        mensagem_traducao.place(x=0, y=180) 


teste = Programa()
teste.cabecalho()
teste.corpo()
teste.janela.mainloop()
        