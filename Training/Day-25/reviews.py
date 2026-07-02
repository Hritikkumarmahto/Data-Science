review=[
  {
    "negative":"this is vary bad product i ordered one month ago",
    "positive": " this product is very good go for it ",
    "bad_products":["shoes","cricket bat"],
    "good_products":["books","mobile","phone"]
  }
]


with open ("positive_review.txt","w") as positivetxt,\
  open("negative_reviews.txt","w") as nengativetxt:

  for item in review:
    for key,value in item.items():

      if key=="positive" or key=="good_products":
        positivetxt.write(f"{key},{value}\n")
      elif key=="negative" or key=="bad_products":
        nengativetxt.write(f"{key},{value}\n")

