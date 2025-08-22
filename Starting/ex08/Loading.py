def ft_tqdm(lst) -> None:
    for item in lst:
        pourcentage = round(item * 100 / lst[-1]) if lst[-1] != 0 else 100
        print(
            f"{' ' * (3 - len(str(pourcentage)))}{pourcentage}%|"
            f"{'█' * pourcentage}{' ' * (100 - pourcentage)}| "
            f"{item + 1}/{lst[-1] + 1}",
            end='\r'
        )
        yield item
