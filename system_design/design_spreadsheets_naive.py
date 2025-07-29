class Spreadsheet:

    def __init__(self, rows: int):
        header = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
        data = [[0] * 26 for _ in range(rows)]

        self.table = [header] + data

    def setCell(self, cell: str, value: int) -> None:
        col, row = int(ord(cell[0]) - ord('A')), int(cell[1:])
        self.table[row][col] = value

    def resetCell(self, cell: str) -> None:
        col, row = int(ord(cell[0]) - ord('A')), int(cell[1:])
        self.table[row][col] = 0

    def getValue(self, formula: str) -> int:
        parts = [t.strip() for t in formula.lstrip('=').split('+')]
        x, y = parts[0], parts[1]  #format "=X+Y"

        # Evaluate left token
        if x.isdigit():
            vx = int(x)
        else:
            col_x, row_x = ord(x[0]) - ord('A'), int(x[1:])  # row is 1..rows
            vx = self.table[row_x][col_x]

        # Evaluate right token
        if y.isdigit():
            vy = int(y)
        else:
            col_y, row_y = ord(y[0]) - ord('A'), int(y[1:])  # row is 1..rows
            vy = self.table[row_y][col_y]

        return vx + vy
        


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)
