# -*- coding:utf-8 -*-
"""Insert int sqlite."""
import sqlite3


def get_tbl(name):
    if name == 'VALLUSERS2U':
        return "insert into vallusers2u values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,\
                  ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,\
                  ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,\
                  ?, ?, ?, ?, ?, ?, ?)"
    elif name == "VUSERS":
        return "insert into vusers values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,\
                  ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,\
                  ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
    else:
        return "insert into vroleuser values (?, ?, ?, ?, ?, ?)"


def get_items(line):
    ret = []
    item = ""
    for it in line.split(","):
        item += it
        if item == "":
            item += ','
        elif item == 'null':
            ret.append("")
            item = ""
        elif item[-1] == "'" and item.count("'") % 2 == 0:
            ret.append(item.strip()[1:-1])
            item = ""
        else:
            item += ','
    return ret


def main():
    # create sqlite engeen
    conn = sqlite3.connect('D:\\sqlite-tools\\SQLiteDatabaseBrowserPortable\\DB2.db')
    c = conn.cursor()
    sql = ""
    # read data from file
    with open('D:\\tmp\\ENT5001B_OUT') as f:
        for line in f.readlines():
            if line[0] != '(':
                if line.split(':')[0] == 'Table':
                    sql = get_tbl(line.split(':')[1][:-1])
                    print(line.split(':')[1])
            else:
                c.execute(sql, get_items(line[1:-2]))
    conn.commit()
    conn.close()

if __name__ == '__main__':
    # unittestを実行
    main()