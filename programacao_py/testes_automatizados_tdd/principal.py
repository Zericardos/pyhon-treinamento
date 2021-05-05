from leilao import Usuario, Lance, Leilao


jose = Usuario('José', 200)
keith = Usuario('Keith', 1000)

lance_keith = Lance(keith, 789.0)
lance_jose = Lance(jose, 150.0)

leilao = Leilao('Celular')

leilao.lances.append(lance_jose)
leilao.lances.append(lance_keith)

"""Se alterarmos a ordem do append, e mantermos if/elif na classe Avaliador,
teremos um problema com os valores esperados. O programa roda, mas não retorna
os valores corretos dos lances"""

for lance in leilao.lances:
    print(f"O usuário {lance.usuario.nome} deu o lance de "
          f"{lance.valor:.2f} reais")


print(f"O menor lance foi de {leilao.menor_lance:.2f} e o maior lance foi"
      f" de {leilao.maior_lance:.2f}")
