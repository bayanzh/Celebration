import tkinter as tk

text_to_animate= '''
           _..._  ,s$$$s.                                                                                          _..._  ,s$$$s.
         .$$$$$$$s$$ss$$$$,                                                                                     .$$$$$$$s$$ss$$$$,
         $$$sss$$$$s$$$$$$$                                                                                     $$$sss$$$$s$$$$$$$
         $$ss$$$$$$$$$$$$$$                                   (             )                                   $$ss$$$$$$$$$$$$$$
         '$$$s$$$$$$$$$$$$'                           )      (*)           (*)      (                           '$$$s$$$$$$$$$$$$'
          '$$$$$$$$$$$$$$'                           (*)      |             |      (*)                           '$$$$$$$$$$$$$$'
            S$$$$$$$$$$$'                             |      |~|           |~|      |                              S$$$$$$$$$$$'
             '$$$$$$$$$'                             |~|     | |           | |     |~|                              '$$$$$$$$$'
               '$$$$$'                               | |     | |           | |     | |                                '$$$$$'
                '$$$'                               ,| |a@@@@| |@@@@@@@@@@@| |@@@@a| |.                                '$$$'
                  ;                            .,a@@@| |@@@@@| |@@@@@@@@@@@| |@@@@@| |@@@@a,.                            ;
                 ;                           ,a@@@@@@| |@@@@@@@@@@@@.@@@@@@@@@@@@@@| |@@@@@@@a,                         ; 
                 ;                          a@@@@@@@@@@@@@@@@@@@@@' . `@@@@@@@@@@@@@@@@@@@@@@@@a                        ;
                 ',                         ;`@@@@@@@@@@@@@@@@@@'   .   `@@@@@@@@@@@@@@@@@@@@@';                        ',
                  ;                         ;@@@`@@@@@@@@@@@@@'     .     `@@@@@@@@@@@@@@@@'@@@;                         ;
                 ,'                         ;@@@;,.aaaaaaaaaa       .       aaaaa,,aaaaaaa,;@@@;                        ,'
                 ;                          ;;@;;;;@@@@@@@@;@      @.@      ;@@@;;;@@@@@@;;;;@@;                        ;
                 ',                         ;;;;;;;@@@@;@@;;@    @@ . @@    ;;@;;;;@@;@@@;;;;;;;                        ',
                  ',                        ;;;;;;;;@@;;;;;;;  @@   .   @@  ;;;;;;;;;;;@@;;;;@;;                         ',
                   ;                        ;;;;;;;;;;;;;;;;;@@     .     @@;;;;;;;;;;;;;;;;@@@;                          ;
                  '                     ,%%%;;;;;;;;@;;;;;;;;       .       ;;;;;;;;;;;;;;;;@@;;%%%,                      '
                                     .%%%%%%;;;;;;;@@;;;;;;;;     ,%%%,     ;;;;;;;;;;;;;;;;;;;;%%%%%%,
                                    .%%%%%%%;;;;;;;@@;;;;;;;;   ,%%%%%%%,   ;;;;;;;;;;;;;;;;;;;;%%%%%%%,
                                    %%%%%%%%`;;;;;;;;;;;;;;;;  %%%%%%%%%%%  ;;;;;;;;;;;;;;;;;;;'%%%%%%%%
                                    %%%%%%%%%%%%`;;;;;;;;;;;;,%%%%%%%%%%%%%,;;;;;;;;;;;;;;;'%%%%%%%%%%%%
                                    `%%%%%%%%%%%%%%%%%,,,,,,,%%%%%%%%%%%%%%%,,,,,,,%%%%%%%%%%%%%%%%%%%%'
                                      `%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%'
                                          `%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%'
                                                 """"""""""""`,,,,,,,,,'""""""""""""""
                                                                `%%%%%%%'
                                                                 `%%%%%'
                                                                   %%% 
                                                                  %%%%%
                                                               .,%%%%%%%,.
                                                          ,%%%%%%%%%%%%%%%%%%%,"""

  ░█████╗░░█████╗░███╗░░██╗░██████╗░██████╗░░█████╗░████████╗██╗░░░██╗██╗░░░░░░█████╗░████████╗██╗░█████╗░███╗░░██╗░██████╗
  ██╔══██╗██╔══██╗████╗░██║██╔════╝░██╔══██╗██╔══██╗╚══██╔══╝██║░░░██║██║░░░░░██╔══██╗╚══██╔══╝██║██╔══██╗████╗░██║██╔════╝
  ██║░░╚═╝██║░░██║██╔██╗██║██║░░██╗░██████╔╝███████║░░░██║░░░██║░░░██║██║░░░░░███████║░░░██║░░░██║██║░░██║██╔██╗██║╚█████╗░
  ██║░░██╗██║░░██║██║╚████║██║░░╚██╗██╔══██╗██╔══██║░░░██║░░░██║░░░██║██║░░░░░██╔══██║░░░██║░░░██║██║░░██║██║╚████║░╚═══██╗
  ╚█████╔╝╚█████╔╝██║░╚███║╚██████╔╝██║░░██║██║░░██║░░░██║░░░╚██████╔╝███████╗██║░░██║░░░██║░░░██║╚█████╔╝██║░╚███║██████╔╝
  ░╚════╝░░╚════╝░╚═╝░░╚══╝░╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░░╚═════╝░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░╚════╝░╚═╝░░╚══╝╚═════╝░

               ░██████╗░██████╗░░█████╗░██████╗░██╗░░░██╗░█████╗░████████╗██╗░█████╗░███╗░░██╗██╗ 
               ██╔════╝░██╔══██╗██╔══██╗██╔══██╗██║░░░██║██╔══██╗╚══██╔══╝██║██╔══██╗████╗░██║██║
               ██║░░██╗░██████╔╝███████║██║░░██║██║░░░██║███████║░░░██║░░░██║██║░░██║██╔██╗██║██║
               ██║░░╚██╗██╔══██╗██╔══██║██║░░██║██║░░░██║██╔══██║░░░██║░░░██║██║░░██║██║╚████║╚═╝
               ╚██████╔╝██║░░██║██║░░██║██████╔╝╚██████╔╝██║░░██║░░░██║░░░██║╚█████╔╝██║░╚███║██╗
               ░╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░░╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░╚════╝░╚═╝░░╚══╝╚═╝
'''
def animate_text(label, text, index=0):


    if index <= len(text):
        label.config(text=text[:index])  
        label.after(5, animate_text, label, text, index + 1)  


window = tk.Tk()
window.configure(bg="black")

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window.geometry(f"{screen_width}x{screen_height}+0+0")

label = tk.Label(window, text="", font=("Courier", 12), fg="pink", bg="black", justify="left")
label.pack(padx=20, pady=20, fill="both", expand=True)

animate_text(label, text_to_animate)

window.mainloop()
