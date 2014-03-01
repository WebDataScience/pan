package spellcheck;

import java.io.IOException;
import java.util.List;

import org.languagetool.JLanguageTool;
import org.languagetool.language.BritishEnglish;
import org.languagetool.language.Spanish;
import org.languagetool.rules.RuleMatch;

public class Spellcheck {

	public int doSpellCheck(String text, String language) {

		if (language.equals("en")) {
			return callEnglishCheck(text);
		} else {
			return callSpanishCheck(text);
		}
	}

	private int callEnglishCheck(String text) {

		int output = 0;
		try {

			JLanguageTool langTool = new JLanguageTool(new BritishEnglish());
			langTool.activateDefaultPatternRules();
			List<RuleMatch> matches = langTool.check(text);

			for (RuleMatch match : matches) {
				if (match.getMessage().equals("Possible spelling mistake found")
						|| match.getMessage().equals("Spelling mistake")
						|| match.getMessage().equals("Possible spelling mistake (without suggestions)")
						|| match.getMessage().equals("Possible spelling mistake")) {
					System.out.println("hereee");
					output++;
				}
			}

		} catch (Exception e) {
			System.out.println("exception in checking english");
		}
		return output;
	}

	private int callSpanishCheck(String text) {
		int output = 0;
		try {

			JLanguageTool langTool = new JLanguageTool(new Spanish());
			langTool.activateDefaultPatternRules();
			List<RuleMatch> matches = langTool.check(text);

			for (RuleMatch match : matches) {
				if (match.getMessage().equals("Hallado un posible error de ortografía")
						|| match.getMessage().equals("Error de ortografía")
						|| match.getMessage().equals("Posible error de ortografía (sin sugerencias)")
						|| match.getMessage().equals("Posible error de ortografía")) {
					output++;
				}
				// Possible typo: you repeated a whitespace

			}

		} catch (Exception e) {
			System.out.println("exception in checking Spanish");
		}
		return output;
	}
	
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		Spellcheck s = new Spellcheck();
		int errors = 0;
		errors = s.doSpellCheck("how are u i m gud", "eng");
		System.out.println("error count:" + errors);
		errors = s.doSpellCheck("¿cómoo sestás", "es");
		System.out.println("error count:" + errors);
	}
}
