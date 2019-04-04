# Задание по работе со скриптами

Программа должна при запускать скрипт, название которого передается программе в качестве аргумента запуска. Скрипты либо для `bash` либо для `cmd` в зависимости от системы

Пример скрипта, который может лежат в таком файле

```Bash
#!/bin/bash

echo "Hello world"
```

Или для `cmd` 
```Cmd
@echo off
echo Hello world
```

Программа должна запускаться с помощью

```Python
if __name__ == "__main__":
	try:
		start(sys.argv[1])
	except:
		...
```

Должны быть реализованы собственные классы исключений. Проблемами могут быть - отсутствие срипта с указанным название, неправильно расширение у файла и т.д. 

Программа должна автоматически определять операционную систему и работать с ".sh" и ".bat" файлами соответсвенно

## Премечание

Башевские файлы запускаются с помощью `./script.sh`, а для Windows с помощью команды ``