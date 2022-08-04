import Api, cash_on_hand, Profit_and_loss, overhead 
 
from pathlib import Path 
 
 
fp= Path.cwd()/"Summary_report.txt" 
fp.touch() 
 
 
with fp.open(mode='a',encoding='UTF-8',newline='') as file : 
    file.write(f'[REAL TIME CURRENCY CONVERSION RATE] USD1= SGD{Api.Exchange_Rate}') 
    file.write('\n') 
    file.write(f'{overhead.Overhead}') 
    file.write('\n') 
    file.write(f" {cash_on_hand.flag_list[0]}") 
    file.write('\n') 
    file.write(f'{cash_on_hand.flag_list[1]}') 
    file.write('\n') 
    file.write(f'{cash_on_hand.flag_list[2]}') 
    file.write('\n') 
    file.write(f'{cash_on_hand.flag_list[3]}') 
    file.write('\n') 
    file.write(f'{cash_on_hand.flag_list[4]}') 
    file.write('\n') 
    file.write(f'{Profit_and_loss.flag_list[0]}') 
    file.write('\n') 
    file.write(f'{Profit_and_loss.flag_list[1]}') 
    file.write('\n') 
    file.write(f'{Profit_and_loss.flag_list[2]}') 
    file.write('\n') 
    file.write(f'{Profit_and_loss.flag_list[3]}') 
    file.write('\n') 
    file.write(f'{Profit_and_loss.flag_list[4]}')

