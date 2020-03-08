import click

@click.command()
def cli():
    """LGTM画像生成ツール"""
    lgtm()
    click.echo('たたかれたよ') #動作確認用

def cli_niwa():
    click.echo('にわたたかれたよ') 

def lgtm():

    #ここにロジックを書く
    click.echo('メインよばれたよ')