import sqlite3
import random
import os

banco = sqlite3.connect("alunos.db")
cursor = banco.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS chamada_alunos ('aluno'	TEXT,'num_chamada' INTEGER PRIMARY KEY AUTOINCREMENT)")

def limpar():
    command = 'cls' if os.name == 'nt' else 'clear'
    os.system(command)

alunos_nomes = ["Denji", 
                "Marceline", 
                "Gwendoly Poole", 
                "James Wattson", 
                "Percy Jackson", 
                "Waly West", 
                "Laura", 
                "Nathiel Phillipes", 
                "Shang Chi", 
                "Yumiko Akame", 
                "Zuri Baraka", 
                "Alexandru Popa", 
                "Oliver Smith", 
                "Ivan", 
                "Shigeo Kageyama", 
                "Ayna Niyazon", 
                "Nanaue", 
                "Yelena Way",
                "Daniel Duarte Dantas"]
class Aluno():
    def inicializacao(self):
        alunos_chamada = random.sample(alunos_nomes, len(alunos_nomes))
        for i in alunos_chamada:
            cursor.execute("INSERT INTO chamada_alunos (aluno) VALUES (?)", (i,))
        banco.commit()

    def aluno_random(self):
        num_indexrandom = random.randrange(1, 19)
        cursor.execute("SELECT * FROM chamada_alunos WHERE num_chamada = (?)", (num_indexrandom,))
        resultado = cursor.fetchone()

        print(f"{resultado[0]}")
    
    def escolher_entre2alunos(self):
        impar = input("IMPAR, ALUNO 1: ")
        par = input("PAR, ALUNO 2: ")

        num = random.randrange(1, 7)

        if num % 2 == 0:
            print(par) 
        else:
            print(impar)


alunos = Aluno()

def main():
    resposta = 0
    while True:
        cursor.execute("SELECT COUNT(*) FROM chamada_alunos")
        valores = cursor.fetchone()[0]

        if valores > 0:
            print(f"BANCO CRIADO: {True}")

        else:
            print(f"BANCO CRIADO: {False}")

        resposta = int(input("1- Inciar Programa\n2- Escolher um aluno aleatório\n3- Decidir batalha NPC\n->"))

        if resposta == 1:
            limpar()
            alunos.inicializacao()

        elif resposta == 2:
            limpar()
            alunos.aluno_random()
        
        elif resposta == 3:
            limpar()
            alunos.escolher_entre2alunos()

if __name__ == "__main__":
    main()