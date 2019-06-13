x=1; for i in *jpg; do counter=$(printf %03d $x); ln "$i" /tmp/img"$counter".jpg; x=$(($x+1)); done
ffmpeg -f image2 -i /tmp/img%03d.jpg /tmp/a.mpg
