pid="$(lsof -ti :8085)"
kill -9 $pid