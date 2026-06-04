        .data #preparação das frases exibidas na execução
prompt: .asciiz "Digite um numero maior que zero: "
erro:   .asciiz "Numero invalido! Tente de novo.\n"
sim:    .asciiz "O numero e octal.\n"
nao:    .asciiz "O numero nao e octal.\n"
 
        .text
        .globl main
main:
 
#chamando prompt, exibindo, lendo a resposta e analisando
ler:
        li   $v0, 4
        la   $a0, prompt
        syscall
 
        li   $v0, 5
        syscall
        move $t0, $v0
 
        bgtz $t0, ok
        li   $v0, 4
        la   $a0, erro
        syscall
        j    ler

#se for maior que 0
ok:
        move $t1, $t0

#se não for (calculos de verificação)
repete:
        beqz $t1, octal
        li   $t2, 10
        div  $t1, $t2
        mfhi $t3
        mflo $t1
        li   $t4, 8
        bge  $t3, $t4, nao_octal
        j    repete

#se for octal 
octal:
        li   $v0, 4
        la   $a0, sim
        syscall
        j    fim

#se não for 
nao_octal:
        li   $v0, 4
        la   $a0, nao
        syscall

#fim do codigo 
fim:
        li   $v0, 10
        syscall