for i in range(2,21):
      with open(f"table1/{i}",'w') as f:
        for j in range(1,11):
          #with open(f"table1/{i}",'a') as f:
            f.write(f"{i}X{j}={i*j}\n")
       