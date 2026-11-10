# Parte 1 - Questão 4: Análise das Limitações do Modelo de Geração de Texto (GPT-2)

Análise das limitações técnicas, comportamentais e computacionais do modelo `gpt2` (arquitetura autoregressiva baseada em decoder) utilizado na API FastAPI da Questão 1 para a tarefa de geração de texto.

## 1. Coerência do Texto Gerado

* **Perda de Coesão em Longo Alcance:** O GPT-2 original possui uma janela de contexto (*context window*) limitada a 1024 tokens. Em gerações mais longas, o modelo tende a perder o fio condutor da narrativa, esquecendo premissas estabelecidas no início do texto.
* **Repetição em Loop (*Repetitive Loops*):** Durante a amostragem autoregressiva, o modelo pode entrar em ciclos de repetição de frases ou estruturas sintáticas idênticas, exigindo técnicas adicionais como *repetition penalty* ou *top-k/top-p sampling* para mitigar o problema.
* **Falta de Planejamento Global:** Por gerar texto token por token com base estritamente na probabilidade do próximo termo (*next-token prediction*), o modelo não planeja a estrutura global do parágrafo, podendo mudar de assunto de forma abrupta sem transição lógica.

## 2. Possíveis Falhas e Incoerências Geradas por LLMs

* **Alucinação de Fatos (*Hallucination*):** O modelo gera afirmações falsas, nomes fictícios ou dados incorretos apresentando-os com alto nível de confiança sintática, uma vez que busca a plausibilidade linguística e não a veracidade dos fatos.
* **Contradições Internas:** Em um mesmo texto gerado, o GPT-2 pode negar uma afirmação que ele próprio fez algumas linhas acima, devido à falta de um módulo de checagem lógica ou base de conhecimento externa.
* **Sensibilidade ao *Prompting*:** Pequenas alterações na frase de entrada (*prompt*) podem resultar em saídas completamente diferentes em tom, qualidade e relevância, demonstrando a ausência de uma compreensão conceitual profunda.

## 3. Desempenho e Questões de Latência

* **Inferência Autoregressiva Lenta:** A geração de texto ocorre token por token (cada token precisa passar por todas as camadas da rede para prever o próximo). Esse processo sequencial impede a paralelação total do cálculo, elevando a latência por requisição.
* **Consumo de Recursos Computacionais:** Mesmo a versão base do GPT-2 exige uso intensivo de memória RAM e processamento matemático. Executar a inferência em CPU gera tempos de resposta altos para o usuário final em chamadas da API.
* **Bloqueio de Concorrência na API:** Sem o uso de processamento assíncrono avançado (*offloading* para *workers* de background ou servidores de inferência dedicados), requisições simultâneas de geração de texto podem travar o *event loop* do FastAPI.

## 4. Limitações na Geração de Conteúdo Apropriado

* **Ausência de Alinhamento (RLHF):** O GPT-2 base é um modelo apenas pré-treinado em dados brutos da internet, sem ter passado por etapas modernas de alinhamento como Aprendizado por Reforço com Feedback Humano (*RLHF*) ou *Instruction Tuning*.
* **Propagação de Vieses e Preconceitos:** O modelo reflete e amplifica vieses implícitos no corpus de treinamento (como estereótipos de gênero, raça ou linguagem tóxica e ofensiva).
* **Falta de Filtros de Segurança Integrados:** Diferente de LLMs comerciais mais recentes, o modelo base não possui guardrails nativos para recusar a geração de conteúdo sensível, desinformação, discurso de ódio ou instruções prejudiciais.