<h2>Trabalho 1 – Manipulação de números binários:</h2>
	<p>A proposta deste trabalho é avaliar o entendimento da manipulação de valores representados de forma binária (base 2). Para isso, o aluno deverá implementar um programa que receba valores de entrada de um arquivo texto representados utilizando 32bits e realizar diferentes operações e manipulações com esses valores. O programa deverá ser capaz de interpretar os valores de entrada como valores inteiros com sinal e magnitude e complemento de 2. O programa também deverá ser capaz de realizar operações de soma e subtração em SM e C2. Os algoritmos de soma e subtração devem ser para SM e C2 (não converta para decimal para fazer as contas). As respostas do programa deverão ser expressas tanto em base binária quanto em base decimal.</p>
	<br>
  <p>A execução do programa deverá obedecer ao seguinte padrão: O programa deverá ler os valores do arquivo de entrada 2 a 2 (cada par é separado por uma linha em branco). O nome do arquivo é parâmetro de entrada informado no momento da execução do script (ex: python trab.py entrada.txt). A saída é impressa na saída padrão (terminal). Em seguida, deverá apresentar esses valores na base 10 utilizando a representação em sinal e magnitude. Após isso, o programa deverá realizar as operações de soma e subtração dos valores como sinal e magnitude, nessa ordem, e exibir seus resultados tanto na base 2 quanto na base 10.  Depois, deverá repetir os passos anteriores utilizando uma representação em complemento de 2. A execução termina quando não houver mais informações a serem lidas no arquivo.</p>
	<br>
  <p>O programa deverá ser desenvolvido utilizando a linguagem de programação Python. Não será permitido o uso de bibliotecas e pacotes que auxiliem na conversão direta dos valores, cabendo aos alunos realizar a manipulação dos dados para a obtenção dos resultados. A avaliação do trabalho consiste na obtenção dos valores corretos de cada operação requisitada, bem como na análise do código desenvolvido.</p>
<h5>Exemplo de entrada (DEVE SER EXATAMENTE ASSIM):</h5>
<p>10000000000000000000000000001011</p>
<p>00000000000000000000000000001010</p>
<h5>Exemplo de saída (DEVE SER EXATAMENTE ASSIM):</h5>
<p>-11</p>
<p>10</p>
<br>
<p>10000000000000000000000000000001</p>
<p>10000000000000000000000000010101</p>
<br>
<p>-1</p>
<p>-21</p>
<br>
<p>-2.147.483.637</p>
<p>10</p>
<br>
<p>10000000000000000000000000010101</p>
<p>10000000000000000000000000000001</p>
<br>
<p>-2.147.483.627</p>
<p>-2.147.483.647</p>
