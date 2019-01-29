import DATA
import xlwt


def fill_table(xijia_, xijia_line, i):
    j=17;
    k=14;
    xijia_.write(xijia_line, 1, DATA.SJ17[i][1]);
    xijia_.write(xijia_line, 2, DATA.SJ17[i][4]);
    xijia_.write(xijia_line, 3, DATA.SJ17[i][5]);
    xijia_.write(xijia_line, 4, DATA.SJ17[i][6]);
    xijia_.write(xijia_line, 5, DATA.SJ17[i][7]);
    xijia_.write(xijia_line, 6, DATA.SJ17[i][15]);
    xijia_.write(xijia_line, 7, DATA.SJ17[i][16]);
    xijia_.write(xijia_line, 8, DATA.SJ17[i][8]);
    xijia_.write(xijia_line, 9, DATA.SJ17[i][9]);
    xijia_.write(xijia_line, 10, DATA.SJ17[i][10]);
    xijia_.write(xijia_line, 11, DATA.SJ17[i][13]);
    xijia_.write(xijia_line, 12, DATA.SJ17[i][11]);
    xijia_.write(xijia_line, 13, DATA.SJ17[i][12]);
    while j<=51:
        xijia_.write(xijia_line, k, DATA.SJ17[i][j]);
        j = j + 1;
        k = k + 1;
    print('hello');

xijia = 1;
xiyi = 16;
yingchao = 3;
yingguan = 9;
yijia = 4;
yiyi = 12;
dejia = 2;
fajia = 5;
file = xlwt.Workbook();
xijia_ = file.add_sheet('xijia', cell_overwrite_ok=True);
xiyi_ = file.add_sheet('xiyi', cell_overwrite_ok=True);
yingchao_ = file.add_sheet('yingchao', cell_overwrite_ok=True);
yingguan_ = file.add_sheet('yingguan', cell_overwrite_ok=True);
yijia_ = file.add_sheet('yijia', cell_overwrite_ok=True);
yiyi_ = file.add_sheet('yiyi', cell_overwrite_ok=True);
dejia_ = file.add_sheet('dejia', cell_overwrite_ok=True);
fajia_ = file.add_sheet('fajia', cell_overwrite_ok=True);


xijia_line = 1;
xiyi_line = 1;
yijia_line = 1;
yiyi_line = 1;
yingchao_line = 1;
yingguan_line = 1;
dejia_line = 1;
fajia_line = 1;

Total = 100;
i = 0;
for i in range(len(DATA.SJ17)):
    print(i);
    if(DATA.SJ17[i][16] == xijia):
        fill_table(xijia_, xijia_line, i);
        xijia_line = xijia_line + 1;
    elif(DATA.SJ17[i][16] == xiyi):
        fill_table(xiyi_, xiyi_line, i);
        xiyi_line = xiyi_line + 1;
    elif(DATA.SJ17[i][16] == yingchao):
        fill_table(yingchao_, yingchao_line, i);
        yingchao_line = yingchao_line + 1;
    elif(DATA.SJ17[i][16] == yingguan):
        fill_table(yingguan_, yingguan_line, i);
        yingguan_line = yingguan_line + 1;
    elif(DATA.SJ17[i][16] == yijia):
        fill_table(yijia_, yijia_line, i);
        yijia_line = yijia_line + 1;
    elif(DATA.SJ17[i][16] == yiyi):
        fill_table(yiyi_, yiyi_line, i);
        yiyi_line = yiyi_line + 1;
    elif(DATA.SJ17[i][16] == dejia):
        fill_table(dejia_, dejia_line, i);
        dejia_line = dejia_line + 1;
    elif(DATA.SJ17[i][16] == fajia):
        fill_table(fajia_, fajia_line, i);
        fajia_line = fajia_line + 1;
file.save("hhh.xls");
