from Crypto.Util.number import *
import gmpy2
n=8346425840345037198129807199954937513125401478961025053438500009262959483940555502608532588666628916939574878135218855958821064838203228082983723434620238007105016628268464539273261229744292297640361962072437956843948295958466836540951955424109567151570099392506528987866673342131787718676889995125410609830917106914342065379286418563488386309724204814943128871119
e =3
c=890620492926502102321644049026872388378498414827953826131346197384557852833466825919448308696314073085933961953691570137956771071596742543745375687720240553544749955984069277312962665151448350105067655613387030994086162903274410383691948894524235546954806222699808006175418241236189457310283573332687555189286927373038549938732981897169435703218096242083962769102
for i in range(10000000):
    if gmpy2.iroot(c+(n*i),5)[1]:
        print(long_to_bytes(gmpy2.iroot(c+(n*i),5)[0]))
