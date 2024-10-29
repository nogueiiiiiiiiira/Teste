import os
from game.interacoes import interrogar_personagensFase1, interrogar_personagensFase2, interrogar_personagensFase3, interrogar_personagensFase4, interrogar_personagensFase5
from game.utils import escrever_lentamente
import time
 

# Funções das fases
def fase1():
    os.system("cls")
    escrever_lentamente("No reino de Castelon, uma pequena vila medieval é abalada por um assassinato brutal. No coração da vila, em uma estalagem afastada e de má fama, um corpo foi encontrado, sem vida e envolto em mistérios. Você, uma investigadora enigmática que raramente é vista, foi chamada para desvendar o caso.")
    escrever_lentamente("\nVocê é uma investigadora conhecida apenas como Samanta, uma mulher de passado nebuloso e com fama de resolver casos impossíveis. Você não é considerada uma nobre, mas também não é uma plebéia. Suas memórias estão fragmentadas, sua cabeça lateja com uma dor intensa, e seu corpo, ainda que forte, parece envolto em uma névoa de cansaço. Sua última memória é desfocada, mas, mesmo assim, uma mensagem curta e direta surge em sua mente: “É hora de trabalhar”.")
    time.sleep(3)
    os.system("cls")
    
    escrever_lentamente("Você estava sentada à sombra de um velho carvalho quando a chamaram. Uma jovem aldeã com olhos preocupados segurava o manto de lã com força, fitando-a com desconfiança. Ela sabe quem você é. O sol já se escondia entre as colinas, lançando uma luz alaranjada sobre os campos. ")
    escrever_lentamente("\n— Preciso que venha comigo... há algo que precisa ver — disse a jovem, quase em um sussurro.")
    escrever_lentamente("\nA dor na cabeça de você latejava novamente, e sua memória parecia traí-la. Você olhou para a jovem e assentiu, ignorando o desconforto. Caminharam em silêncio até a velha estalagem 'O Corvo e a Espada', um lugar mal-afamado, onde poucos nobres ousavam pisar.")
    escrever_lentamente("\nAssim que cruzou a soleira, o cheiro de sangue a atingiu como um golpe. No centro do salão estava o corpo: Baldwin, o Ferreiro. Ele jazia no chão, com um corte profundo no peito e marcas de luta pelos braços e rosto. Você se abaixou para observar os detalhes, mas não conseguia se livrar da estranha sensação de que havia algo familiar naquele lugar. Era como se cada canto da estalagem, cada passo, cada sombra guardasse um fragmento esquecido de seu próprio passado.")
    escrever_lentamente("\nEnquanto analisava a cena, você encontrou cinco pistas principais:")
    escrever_lentamente("\nUma faca de lâmina fina: cravada na madeira próxima ao corpo, sua lâmina estava levemente torta, indicando uma luta. Mas a faca não parecia algo que Baldwin, o Ferreiro, usaria. Talvez fosse um item de cozinha ou de um caçador?")
    escrever_lentamente("\nMarcas de pegadas: algumas pareciam frescas, vindas da direção da porta dos fundos, enquanto outras eram mais confusas.")
    escrever_lentamente("\nFragmentos de pano vermelho: próximos ao corpo, havia pedaços de tecido fino e vermelho, bem diferente das vestes grosseiras que Baldwin usava.")
    escrever_lentamente("\nUma garrafa quebrada: estilhaçada próxima ao corpo, um cheiro doce e forte exalava do líquido derramado. Provavelmente algum licor caro que só alguém com poder ou influência teria acesso.")
    escrever_lentamente("\nCom essas pistas em mente e com o relato de que o corpo foi achado ao amanhecer, você faz uma lista dos principais suspeitos e se prepara para os interrogatórios. Cada pista levaria a uma fase de investigação com diferentes indivíduos.")
    
    time.sleep(3)
    os.system("cls")
    
    escrever_lentamente("Diana, a Cozinheira da Estalagem: é uma mulher de porte robusto, com braços fortes e mãos marcadas pelo manuseio constante de facas e panelas. Sua expressão é dura, e suas sobrancelhas cerradas passam um ar de desconfiança e irritação. Ela veste um avental de tecido grosso e velho, levemente manchado, indicando as longas horas que passa na cozinha da estalagem. Diana raramente sorri, e seu olhar afiado parece cortar tão fundo quanto as facas que ela domina. Murmura-se que, apesar de seu temperamento difícil, Diana tem um coração bondoso, mas ela é conhecida por sua hostilidade com homens desordeiros, especialmente Baldwin, com quem já teve discussões acaloradas acerca de sua reputação e seu modo de lidar com suas hóspedes femininas.")
    escrever_lentamente("\nErik, o Caçador: é um homem magro e ágil, com olhos afiados como os de uma raposa. Ele usa uma capa marrom suja de terra e folhas, sugerindo que passou a maior parte do dia na floresta. Sempre carrega uma pequena faca de caça presa ao cinto, e suas botas estão cobertas de lama seca. Erik evita contato visual e parece estar sempre inquieto, como se estivesse pronto para desaparecer na floresta a qualquer instante. Embora reservado, os aldeões o respeitam por seu conhecimento das matas e de tudo o que vive nelas, mas sua relação com Baldwin, o ferreiro, era tensa, pois Baldwin costumava atrapalhar seus negócios com armas e mexer com sua esposa.")
    escrever_lentamente("\nMariana, a Donzela da Estalagem: é uma jovem de aparência delicada, com cabelos castanhos trançados e um vestido simples, embora bem cuidado. Ela é ágil e discreta, movendo-se com a graça de alguém acostumada a servir e a observar em silêncio. Mariana tem um semblante nervoso, e seus dedos finos se retorcem enquanto fala, o que sugere que algo a preocupa profundamente. Apesar de jovem, Mariana conhece muitos dos segredos da vila, pois escuta conversas sem ser notada, especialmente na estalagem. Rumores dizem que Baldwin dava alguns avanços indesejados nela.")
    escrever_lentamente("\nBoris, o Guardião da Vila: com uma expressão carrancuda e um corpo grande e musculoso, Boris é a imagem do típico guardião. Suas roupas de couro grosso e suas mãos calejadas mostram que está acostumado a trabalhos pesados. Ele usa uma barba bem aparada, e seus olhos severos revelam uma autoridade silenciosa, que poucos ousam questionar. Boris é direto e econômico nas palavras, falando apenas o necessário. Ele é conhecido por sua lealdade, mas também por seu comportamento discreto e relutante em se envolver em questões alheias. Mais de uma vez, já entrou em brigas e discussões com Baldwin por o mesmo não respeitar as mulheres.")
    escrever_lentamente("\nMadame Lavínia, a Nobre da Vila: é uma mulher de porte elegante, de pele pálida e cabelos loiros finamente arrumados. Veste-se com roupas de linho vermelho e jóias discretas, e é sempre vista com uma postura altiva e fria. Madame Lavínia raramente interage com os aldeões e, embora seja conhecida por sua generosidade, poucos ousam se aproximar dela. Seus olhos calculistas analisam cada movimento seu, como se tentassem prever cada pergunta. Aparentemente, Lavínia guarda rancores, principalmente de Baldwin, por motivos que ninguém suspeito do porquê.")
    escrever_lentamente("\nRodrigo é um homem robusto, com braços fortes e calejados pelo trabalho constante nas tavernas e armazéns. Ele veste roupas simples de couro marrom, manchadas por anos de manipulação de barris de vinho e licores. Uma túnica de linho grosso cobre seu peito, e uma faixa de tecido vermelho em torno da cintura sugere um toque pessoal de orgulho em seu ofício. Seu cabelo é curto e escuro, já mostrando sinais de grisalho nas têmporas, e uma barba rala cobre seu queixo, sempre perfumada pelo leve aroma de especiarias e álcool.")
    time.sleep(3)
    os.system("cls")
    interrogar_personagensFase1()
    pass 

def fase2():
    os.system("cls")
    escrever_lentamente("Após o interrogatório inicial, você reflete sobre o que descobriu. Diana e Erik, os dois que lidavam com facas, mostraram reações diferentes. Diana admitiu ter tido conflitos com Baldwin, e sua irritação ficou evidente, embora ela aparentemente não reconhecesse a faca. Já Erik, que parecia mais cauteloso, também confessou um histórico de desavenças com o ferreiro, embora insistisse que aquele tipo de faca não era seu. As suas suspeitas se intensificam enquanto você se recorda que a lâmina parecia fina, mais próxima de uma faca de cozinha do que de uma arma de caça.")
    escrever_lentamente("\nAs pegadas são o próximo passo a ser investigado; você decide que sua próxima investigação será sobre as pegadas próximas à porta dos fundos e quem poderia ter acesso a esse local.")
    
    time.sleep(3)
    os.system("cls")
    interrogar_personagensFase2()
    pass

def fase3():
    os.system("cls")
    escrever_lentamente("Após conversar com Mariana e Boris, você recolhe mais informações sobre as pegadas na porta dos fundos. Mariana menciona ter visto uma figura saindo apressadamente, mas não conseguiu ver detalhes. Boris, mesmo hesitante, confirma ter avistado alguém encapuzado saindo com algo nas mãos, mas reluta em dar mais detalhes por não ter confiança em suas lembranças.")
    escrever_lentamente("\nAs pegadas eram pequenas e leves. Você sente que alguém está escondendo detalhes importantes e decide seguir a próxima pista: os fragmentos de pano vermelho, o que a leva à figura imponente de Madame Lavínia.")
    
    time.sleep(3)
    os.system("cls")
    interrogar_personagensFase3()
    pass

def fase4():
    os.system("cls")
    escrever_lentamente("Após conversar com Madame Lavínia, que é fria e altiva em suas respostas, você decide seguir adiante com suas investigações.")
    escrever_lentamente("\nA cor e a qualidade do tecido apontam para alguém de recursos ou posição elevada, reforçando a hipótese de uma presença feminina e distinta. Você decide que é hora de investigar a garrafa quebrada e o licor, que talvez possa levá-la a mais informações sobre a possível conexão de Lavínia ou outra pessoa com Baldwin.")
    
    time.sleep(3)
    os.system("cls")
    interrogar_personagensFase4()
    pass

def fase5():
    os.system("cls")
    escrever_lentamente("\nFinalmente, com todas as peças do quebra-cabeças reunidas, você percebe que chegou a hora de escolher um assassino. Você sente que cada detalhe aponta para uma verdade oculta, e a dor de cabeça lateja como um tambor de advertência.")

    time.sleep(3)
    os.system("cls")
    interrogar_personagensFase5()
    pass

