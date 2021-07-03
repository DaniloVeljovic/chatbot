def generate_table(rows, cols):
    table = '<BEFORE><table id = ?>'
    for r in range(rows):
        table += '<tr id = ?>'
        for c in range(cols):
            table += '<td id = ?> <CONTENT> </td>'
        table += '</tr>'
    table += '</table><AFTER>'
    return table
