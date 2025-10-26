# Laboratório com AWS Step Functions

Este repositório documenta uma prática do laboratório da DIO sobre construção de workflows automatizados usando **AWS Step Functions**.  
O objetivo é demonstrar entendimento de orquestração serverless, automação e boas práticas de observabilidade.

---

## Objetivo do Workflow

Em vez de escrever toda a lógica em um único serviço, usei uma **máquina de estados** no Step Functions para coordenar as etapas.

---

## Arquitetura

### Serviços envolvidos
- **AWS Step Functions**: orquestra o fluxo (quem chama quem, em qual ordem).
- **AWS Lambda**: executa lógica de negócio em etapas independentes.

---

## Estrutura da State Machine

A definição da máquina de estados (Amazon States Language - JSON) está em:
[`state-machine/state-machine.json`](./state-machine/state-machine.json)

Principais estados usados:

- **Task State**  
  Executa uma função Lambda específica.  
  Ex.: `ProcessInput`, `ValidateData`, `SaveResult`.

- **Choice State**  
  Desvia o fluxo com base em uma condição.  
  Ex.: se os dados são válidos → continua; se não → vai para tratamento de erro.

- **Catch / Retry**  
  Configurado para lidar com falhas de execução de Lambda sem derrubar todo o fluxo.
