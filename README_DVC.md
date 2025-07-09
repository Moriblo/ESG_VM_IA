# ESG_VM_IA
Branch para utilização do Data Version Control, para facilitar o controle de versionamento de IA

# 🧠 Guia de Versionamento de Projetos de IA com GitHub + DVC

Este guia apresenta um fluxo prático para versionar projetos de machine learning e IA usando GitHub em conjunto com DVC (Data Version Control). Ideal para times que desejam reprodutibilidade, rastreabilidade e colaboração eficiente.

---

## 📦 Pré-requisitos

- Conta no [GitHub](https://github.com)
- Git instalado (`git --version`)
- Python instalado
- DVC instalado (`pip install dvc`)
- Repositório remoto para dados (ex: Google Drive, S3, Azure Blob)

---

## 🛠️ Etapas do Versionamento

### 1. Inicialize o repositório

```bash
git init
dvc init
```

> Isso cria a estrutura básica do projeto com suporte a versionamento de dados.

---

### 2. Adicione os dados ao controle do DVC

```bash
dvc add data/dataset.csv
```

Isso cria um arquivo `dataset.csv.dvc` que rastreia o dataset sem armazená-lo no Git.

```bash
git add data/.gitignore data/dataset.csv.dvc
git commit -m "Adiciona dataset versionado com DVC"
```

---

### 3. Configure o armazenamento remoto para os dados

```bash
dvc remote add -d storage gdrive://<ID-da-pasta>
dvc push
```

> Substitua `gdrive://` por `s3://`, `azure://`, etc., conforme seu provedor.

---

### 4. Crie o pipeline de treino

```bash
dvc stage add -n train \
  -d train.py \
  -d data/dataset.csv \
  -o model.pkl \
  python train.py
```

Isso gera os arquivos `dvc.yaml` e `dvc.lock`.

```bash
git add dvc.yaml dvc.lock train.py
git commit -m "Adiciona pipeline de treino com DVC"
```

---

### 5. Execute e rastreie experimentos

```bash
dvc exp run
dvc exp show
```

> Você pode alterar hiperparâmetros em `params.yaml` e rodar novos experimentos.

---

### 6. Versione métricas e parâmetros

```bash
dvc metrics show
dvc params diff
```

> Use arquivos como `metrics.json` e `params.yaml` para rastrear performance e configurações.

---

### 7. Compartilhe com o time via GitHub

```bash
git push origin main
dvc push  # envia os dados para o armazenamento remoto
```

> Isso garante que o código, os dados e os modelos estejam sincronizados e versionados.

---

## 📁 Estrutura típica do projeto

```
.
├── data/
│   └── dataset.csv
├── model.pkl
├── train.py
├── dvc.yaml
├── dvc.lock
├── params.yaml
├── metrics.json
├── .gitignore
└── .dvc/
```

---

## ✅ Benefícios

- 🔁 Reprodutibilidade total de experimentos
- 📊 Comparação de métricas entre versões
- ☁️ Armazenamento eficiente de grandes arquivos
- 🤝 Colaboração via GitHub com pull requests e CI/CD
- 📂 Separação clara entre código, dados e modelos

---

## 🔗 Recursos úteis

- [Documentação oficial do DVC](https://dvc.org/doc)
- [Exemplo de projeto com DVC + GitHub](https://github.com/iterative/example-get-started)
- [GitHub Actions para DVC](https://github.com/iterative/setup-dvc)
- [Guia de MLOps com DVC](https://dvc.org/doc/use-cases/mlops)
- [AI model performance metrics: in-depth guide](https://nebius.com/blog/posts/ai-model-performance-metrics?form=MG0AV3)

---

> 💡 Dica: Combine DVC com MLflow ou Weights & Biases para rastrear experimentos de forma ainda mais rica e visual.

