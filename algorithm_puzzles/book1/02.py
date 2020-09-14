import re

operators = ['*', '']

def main():
    for i in range(1000, 10000):
        for j in operators:
            for k in operators:
                for l in operators:
                    num = str(i)
                    val = num[3] + j + num[2] + k + num[1] + l + num[0]

                    val = re.sub(r"0(\d+)", r"\1", val)

                    if len(val) > 4:
                        if i == eval(val):
                            print(val, '=', i)

if __name__ == '__main__':
    main()