# ESG_VM_IA
Repository to develop the AI initiatives to ESG Value Mining

# 🌱 ESG_VM_IA

Este repositório contém a estrutura e os experimentos do projeto **ESG Data Mining com IA**, com foco em versionamento de dados, modelos e pipelines utilizando **GitHub + DVC**.

---

## 📌 Objetivo

Correlacionar dados de diferentes fontes (projetos, fundos, geodados) para responder perguntas de stakeholders interessados em investimentos com viés ESG, como:

- Investidores
- ONGs
- Gestores de projeto

---

## 🧠 Tecnologias Utilizadas

- **Python** para scripts de modelagem e análise
- **DVC (Data Version Control)** para versionamento de dados e modelos
- **GitHub** para versionamento de código e colaboração
- **PostgreSQL + PostGIS** (futuramente) para armazenamento geoespacial
- **MLflow** (opcional) para rastreamento de experimentos

---

## 🗂️ Estrutura do Repositório

```
.
├── data/               # Dados de entrada (versionados com DVC)
├── model.pkl           # Modelo treinado
├── train.py            # Script de treino
├── dvc.yaml            # Pipeline de execução
├── dvc.lock            # Versão travada do pipeline
├── params.yaml         # Hiperparâmetros
├── metrics.json        # Métricas de avaliação
├── .dvc/               # Metadados do DVC
└── versionamento-ia-github-dvc.md  # Guia completo de versionamento
```

---

## 🚀 Como usar este repositório

### 1. Clone o projeto

```bash
git clone https://github.com/<seu-usuario>/esg_vm_IA.git
cd esg_vm_IA
```

### 2. Instale as dependências

```bash
pip install -r requirements.txt
pip install dvc
```

### 3. Recupere os dados e modelos

```bash
dvc pull
```

### 4. Execute o pipeline

```bash
dvc repro
```

---

## 📊 Versionamento com DVC

Este projeto utiliza DVC para:

- Versionar datasets e modelos
- Rastrear experimentos e métricas
- Compartilhar dados com segurança via armazenamento remoto

Consulte o arquivo [`versionamento-ia-github-dvc.md`](./versionamento-ia-github-dvc.md) para um guia completo.

---

## 🤝 Contribuindo

Contribuições são bem-vindas! Para colaborar:

1. Faça um fork do projeto
2. Crie uma branch: `git checkout -b minha-feature`
3. Commit suas alterações: `git commit -m 'feat: nova funcionalidade'`
4. Push para sua branch: `git push origin minha-feature`
5. Abra um Pull Request

---

## 📄 Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

---

> Desenvolvido com 💚 para apoiar decisões ESG baseadas em dados.
