# coding: utf-8
def get_table(table_tuple):
    temp = '''
        <table border="1">
            <tr>
                <td>id</td>
                <td>host</td>
                <td>memory</td>
            </tr>
    '''

    for i in table_tuple:
        temp += '''
            <tr>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
            </tr>
        ''' % i

    temp += '</table>'

    return temp
