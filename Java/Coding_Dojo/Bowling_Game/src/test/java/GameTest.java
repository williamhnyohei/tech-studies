import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class GameTest {

    @Test
    public void testAllGutterBalls() {
        Game game = new Game();
        rollMany(game, 20, 0);
        assertEquals(0, game.score());
    }

    private void rollMany(Game game, int rolls, int pins) {
        for (int i = 0; i < rolls; i++) {
            game.roll(pins);
        }
    }
}
