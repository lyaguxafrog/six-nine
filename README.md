# six-nine 6️⃣9️⃣

**Convenient and efficient library for obtaining 69 in various formats**

## Install
```bash
pip install six-nine
```
or using [poetry](https://python-poetry.org/):
```bash
poetry add six-nine
```


## Usage
```python
import sixnine

sn = sixnine.SixNine()


print(sn()) # 69 as str
print(sn.int()) # 69 as int
print(sn.text()) # output "six nine" string
print(sn.bin) # 0b1000101
print(sn.oct()) # 0o105
print(sn.hex()) # 0x45
```
