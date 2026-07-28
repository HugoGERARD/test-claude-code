# Game of Life

Petit projet de test : une implémentation du Jeu de la Vie de Conway en Python, avec grille torique (wrap-around), CLI, et tests unitaires.

## Utilisation

```bash
pip install -r requirements.txt
python -m gameoflife.cli --pattern glider --width 15 --height 10 --generations 30
```

Options :
- `--pattern random|glider` : motif de départ
- `--width`, `--height` : dimensions de la grille
- `--density` : densité initiale de cellules vivantes (motif random)
- `--seed` : graine aléatoire pour reproductibilité
- `--generations` : nombre de générations à simuler
- `--delay` : délai entre générations (secondes)

## Tests

```bash
pytest
```
