# New戦争ゲームを考える
import random

class Ship:
    def __init__(self):
        self.hitpoint = 0
        self.damage = 0
        self.ship_id = 0
        self.name_jp = ""

class Battle_ship(Ship):
    def __init__(self):
        super().__init__()
        self.hitpoint = 50
        self.damage = 12
        self.ship_id = 1
        self.name_jp = "戦艦"

class submarine(Ship):
    def __init__(self):
        super().__init__()
        self.hitpoint = 25
        self.damage = 10
        self.ship_id = 2
        self.name_jp = "潜水艦"

class destroyer(Ship):
    def __init__(self):
        super().__init__()
        self.hitpoint = 25
        self.damage = 6
        self.ship_id = 3
        self.name_jp = "駆逐艦"

class cruiser(Ship):
    def __init__(self):
        super().__init__()
        self.hitpoint = 35
        self.damage = 9
        self.ship_id = 4
        self.name_jp = "巡洋艦"

print("海戦ゲームを開始します")
print("")
print("簡単なゲーム概要を説明します")
print("プレイヤーとディーラーが艦船を選択し、戦闘を行います")
print("艦船はそれぞれ異なる特性を持っています")
print("艦船の種類は戦艦、潜水艦、駆逐艦、巡洋艦の4種類です")
print("")
print("戦艦は駆逐艦に強く、駆逐艦は潜水艦に強く、潜水艦は戦艦に強くなっています\n(相性が良い場合2倍の火力を与えることができますが、相性が悪い場合逆に火力が半減します)")
print("巡洋艦は全ての艦船に対してある程度応戦できる能力を持っていますが、決定打にはなりません")
print("")
print("戦艦:HP50,攻撃力12\n駆逐艦:HP25,攻撃力6\n潜水艦:HP25,攻撃力10\n巡洋艦:HP35,攻撃力9")
print("")
print("")

class Game:
    def game_system_1_for_player(self):  # 修正: selfを追加してインスタンスメソッドに変更
        self.player_ships = []  # プレイヤーの艦隊を保存するリスト
        counter_1 = 0
        print("プレイヤーの艦隊:")
        while counter_1 < 3:  # 修正: ループ条件を修正
            my_ship = random.randint(1, 4)
            if my_ship == 1:
                my_ship = Battle_ship()
                ship_serial = random.randint(1000, 9999)
                counter_1 += 1
            elif my_ship == 2:
                my_ship = submarine()
                ship_serial = random.randint(1000, 9999)
                counter_1 += 1
            elif my_ship == 3:
                my_ship = destroyer()
                ship_serial = random.randint(1000, 9999)
                counter_1 += 1
            elif my_ship == 4:
                my_ship = cruiser()
                ship_serial = random.randint(1000, 9999)
                counter_1 += 1
            ship_container = [my_ship, ship_serial]  # 修正: リストの作成方法を修正
            self.player_ships.append(ship_container)  # 艦隊に追加
            print(f"艦種: {ship_container[0].name_jp}, シリアル番号: {ship_container[1]}")

    def game_system_2_for_dealer(self):
        self.dealer_ships = []  # ディーラーの艦隊を保存するリスト
        self.dealer_serialbox = [] # ディーラーの艦船のシリアル番号のみ保存するリスト
        counter_2 = 0
        print("ディーラーの艦隊:")
        while counter_2 < 3:
            your_ship = random.randint(1, 4)
            if your_ship == 1:
                    your_ship = Battle_ship()
                    ship_serial = random.randint(1000, 9999)
                    self.dealer_serialbox.append(ship_serial)
                    counter_2 += 1
            elif your_ship == 2:
                    your_ship = submarine()
                    ship_serial = random.randint(1000, 9999)
                    self.dealer_serialbox.append(ship_serial)
                    counter_2 += 1
            elif your_ship == 3:
                    your_ship = destroyer()
                    ship_serial = random.randint(1000, 9999)
                    self.dealer_serialbox.append(ship_serial)
                    counter_2 += 1
            elif your_ship == 4:
                    your_ship = cruiser()
                    ship_serial = random.randint(1000, 9999)
                    self.dealer_serialbox.append(ship_serial)
                    counter_2 += 1
            ship_container_2 = [your_ship, ship_serial]
            self.dealer_ships.append(ship_container_2)# ディーラーの艦船のシリアル番号を保存
            print(f"艦種: {ship_container_2[0].name_jp}, シリアル番号: {ship_container_2[1]}")         
    
    def game_system_3_for_player_select(self):
        while True:
            try:
                select = int(input("使用する軍艦のシリアル番号を半角数字で入力: "))
                for ship_container in self.player_ships:
                    if select == ship_container[1]:
                        print(f"選択された艦種: {ship_container[0].name_jp}, シリアル番号: {ship_container[1]}")
                        return ship_container[0]  # 選択された艦船を返す
                print("無効な入力を検出しました。やり直してください。")
            except ValueError:
                print("無効な入力です。数字を入力してください。")

    def game_system_4_for_dealer_select(self):
        if self.dealer_ships:
            select_2 = random.randint(0, len(self.dealer_ships) - 1)
            selected_ship = self.dealer_ships[select_2]
            print(f"ディーラーが選択した艦種: {selected_ship[0].name_jp}, シリアル番号: {selected_ship[1]}")
            return selected_ship[0]  # 選択された艦船を返す
        else:
            print("ディーラーの艦隊は空です。")
            return None

    

    def game_system_5_for_battle(self, player_card, dealer_card):
        player_damage = player_card.damage
        dealer_damage = dealer_card.damage

        # プレイヤーの艦船がディーラーの艦船に与えるダメージを計算
        if isinstance(player_card, Battle_ship) and isinstance(dealer_card, destroyer):
            player_damage *= 2  # 修正: プレイヤーのダメージを2倍
        elif isinstance(player_card, destroyer) and isinstance(dealer_card, submarine):
            player_damage *= 2
        elif isinstance(player_card, submarine) and isinstance(dealer_card, Battle_ship):
            player_damage *= 2
        elif isinstance(player_card, Battle_ship) and isinstance(dealer_card, submarine):
            player_damage *= 0.5  # 修正: プレイヤーのダメージを半減
        elif isinstance(player_card, destroyer) and isinstance(dealer_card, Battle_ship):
            player_damage *= 0.5
        elif isinstance(player_card, submarine) and isinstance(dealer_card, destroyer):
            player_damage *= 0.5

        # ディーラーの艦船がプレイヤーの艦船に与えるダメージを計算
        if isinstance(dealer_card, Battle_ship) and isinstance(player_card, destroyer):
            dealer_damage *= 2  # 修正: ディーラーのダメージを2倍
        elif isinstance(dealer_card, destroyer) and isinstance(player_card, submarine):
            dealer_damage *= 2
        elif isinstance(dealer_card, submarine) and isinstance(player_card, Battle_ship):
            dealer_damage *= 2
        elif isinstance(dealer_card, Battle_ship) and isinstance(player_card, submarine):
            dealer_damage *= 0.5  # 修正: ディーラーのダメージを半減
        elif isinstance(dealer_card, destroyer) and isinstance(player_card, Battle_ship):
            dealer_damage *= 0.5
        elif isinstance(dealer_card, submarine) and isinstance(player_card, destroyer):
            dealer_damage *= 0.5

        # プレイヤーの選択した艦船にダメージを適用
        player_card.hitpoint -= dealer_damage
        print(f"ディーラーの {dealer_card.name_jp} がプレイヤーの {player_card.name_jp} に {dealer_damage} のダメージを与えました。")
        if player_card.hitpoint <= 0:
            print(f"プレイヤーの {player_card.name_jp} は沈没しました。")
            self.player_ships = [ship for ship in self.player_ships if ship[0] != player_card]

        # ディーラーの選択した艦船にダメージを適用
        dealer_card.hitpoint -= player_damage
        print(f"プレイヤーの {player_card.name_jp} がディーラーの {dealer_card.name_jp} に {player_damage} のダメージを与えました。")
        if dealer_card.hitpoint <= 0:
            print(f"ディーラーの {dealer_card.name_jp} は沈没しました。")
            self.dealer_ships = [ship for ship in self.dealer_ships if ship[0] != dealer_card]

        while True:
            if not self.player_ships:
                print("プレイヤーの艦隊は全滅しました。ディーラーの勝利！")
                return True  # 戦闘終了
            elif not self.dealer_ships:
                print("ディーラーの艦隊は全滅しました。プレイヤーの勝利！")
                return True  # 戦闘終了
            else:
                print("戦闘を継続します。")
                # プレイヤーとディーラーの艦船を選択
                print("プレイヤーの艦船情報:")
                for ship_container in self.player_ships:
                 print(f"艦種: {ship_container[0].name_jp}, シリアル番号: {ship_container[1]}, HP: {ship_container[0].hitpoint}, 攻撃力: {ship_container[0].damage}")
                print("")
                # ディーラーの艦船情報を表示
                print("ディーラーの艦船情報:")
                for ship_container_2 in self.dealer_ships:
                 print(f"艦種: {ship_container_2[0].name_jp}, HP: {ship_container_2[0].hitpoint},")        
                print("")
                player_card = self.game_system_3_for_player_select()
                dealer_card = self.game_system_4_for_dealer_select()
                # 戦闘を実行
                self.game_system_5_for_battle(player_card, dealer_card)                  
       
# 修正: Gameクラスのインスタンスを作成してメソッドを呼び出す
if __name__ == "__main__":
    game = Game()
    game.game_system_1_for_player()
    print("")
    game.game_system_2_for_dealer()
    print("")
    game.game_system_3_for_player_select()
    print("")
    game.game_system_4_for_dealer_select()
    print("")
    game.game_system_5_for_battle(game.player_ships[0][0], game.dealer_ships[0][0])  # 戦闘を開始