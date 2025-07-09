# Exemplo completo de um script train.py que:
# ✅ Lê os hiperparâmetros do arquivo params.yaml usando PyYAML
# ✅ Treina um modelo de classificação com scikit-learn
# ✅ Salva o modelo treinado como model.pkl
# ✅ Calcula e salva métricas em metrics.json (como accuracy)
# ✅ Requisitos para rodar:
# Certifique-se de que o seu dataset.csv tenha uma coluna chamada target e que as demais colunas sejam numéricas ou já estejam tratadas.

import yaml
import pandas as pd
import json
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score

# 1. Carrega os parâmetros do arquivo params.yaml
with open("params.yaml", "r") as f:
    params = yaml.safe_load(f)["train"]

# 2. Carrega os dados
df = pd.read_csv("data/dataset.csv")

# 3. Pré-processamento simples (exemplo)
X = df.drop("target", axis=1)
y = df["target"]

# 4. Divide os dados
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=params["test_size"],
    random_state=params["random_state"]
)

# 5. Treina o modelo
model = GradientBoostingClassifier(
    n_estimators=params["n_estimators"],
    max_depth=params["max_depth"],
    learning_rate=params["learning_rate"],
    random_state=params["random_state"]
)
model.fit(X_train, y_train)

# 6. Avalia o modelo
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

# 7. Salva o modelo
joblib.dump(model, "model.pkl")

# 8. Salva as métricas
metrics = {"accuracy": accuracy}
with open("metrics.json", "w") as f:
    json.dump(metrics, f, indent=4)

print(f"Modelo treinado com accuracy: {accuracy:.4f}")
