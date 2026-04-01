# Calculadora de Bhaskara

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![License](https://img.shields.io/badge/license-MIT-green?style=for-the-badge)

Uma ferramenta simples e eficiente desenvolvida em Python para resolver equações do segundo grau utilizando a Fórmula de Bhaskara. O script calcula o discriminante ($\Delta$) e retorna as raízes reais de forma automática.

## 🎯 Objetivo do Projeto
Este script foi criado para automatizar o cálculo de raízes matemáticas, lidando com:
* Validação de divisões por zero ($a = 0$).
* Identificação de raízes inexistentes no conjunto dos números reais ($\Delta < 0$).
* Cálculo de raízes únicas ($\Delta = 0$) e raízes distintas ($\Delta > 0$).

## 🧮 A Lógica Matemática
O programa resolve equações no formato $ax^2 + bx + c = 0$, baseando-se em:

1. **Delta:** $\Delta = b^2 - 4ac$
2. **Bhaskara:** $x = \frac{-b \pm \sqrt{\Delta}}{2a}$

## 🚀 Como Executar

1. **Pré-requisitos:** Ter o [Python 3.x](https://www.python.org/) instalado.
2. **Clone o repositório:**
   ```bash
   git clone [https://github.com/seu-usuario/nome-do-repositorio.git](https://github.com/seu-usuario/nome-do-repositorio.git)
