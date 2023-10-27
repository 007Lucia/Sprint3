echo. ##############TEST PATH #############
cd ./Tests
python -m pytest tst_1054.py tst_1055.py tst_1056.py --html=../Results/RossoLucia.html --self-contained-html
pause
