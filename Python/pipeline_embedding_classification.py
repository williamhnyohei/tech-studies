# Instale antes:
# !pip install sentence-transformers scikit-learn pandas

from sentence_transformers import SentenceTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.preprocessing import LabelEncoder
import pandas as pd

# 1. Dados simulados
reviews = [
    "Produto excelente, entrega rápida",
    "Nota 5, mas veio quebrado",
    "Design bonito, muito satisfeito",
    "Veio riscado e demorou para chegar",
    "Atendimento perfeito e produto de qualidade",
    "Horrível, nota alta mas tudo errado",
    "Ótima experiência, recomendo",
    "Chegou com defeito, mas dei nota 5",
]

labels = [
    "positivo",
    "negativo",
    "positivo",
    "negativo",
    "positivo",
    "negativo",
    "positivo",
    "negativo"
]

# 2. Embeddings
model = SentenceTransformer("all-MiniLM-L6-v2")
X = model.encode(reviews)

# 3. Rótulos numéricos
encoder = LabelEncoder()
y = encoder.fit_transform(labels)

# 4. Treinar modelo
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)
clf = LogisticRegression(max_iter=1000)
clf.fit(X_train, y_train)

# 5. Avaliação
y_pred = clf.predict(X_test)
report = classification_report(y_test, y_pred, target_names=encoder.classes_)
print(report)
