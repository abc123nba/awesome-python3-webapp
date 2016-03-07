git add 无法直接添加空目录
解决办法：add一个空目录，在它下面touch一个.gitignore文件。
touch a
vi a
git add a
git commit -m  "add a"
git remote add origin git@github.com:XX/XX.git
git push origin masters

touch .gitignore
cd  /
cd ..
ls
