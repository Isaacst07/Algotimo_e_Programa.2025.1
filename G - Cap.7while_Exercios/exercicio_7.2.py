import math 

def main():
    
    print("Digite expressões (ex: 1 + 2, math.sqrt(9)). Digite 'fim' para encerrar.")

    expressions = []
    while True:
        expr = input(">>> ")
        expressions.append(expr)
        if expr.strip().lower() == 'fim':
            break

    resultado_final = eval_loop(expressions)
    print(f"\nÚltimo resultado avaliado (antes de 'done'): {resultado_final}")


def eval_loop(expressions):
    last_result = None
    index = 0
    while index < len(expressions):
        expr = expressions[index].strip()
        if expr.lower() == 'done':
            break
        try:
            last_result = eval(expr)
            print(f"Resultado: {last_result}")
        except Exception as e:
            print(f"Erro ao avaliar '{expr}': {e}")
        index += 1
    return last_result


main()