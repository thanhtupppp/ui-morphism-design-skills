import React from 'react';
import { Pressable, StyleSheet, Text, useWindowDimensions, View } from 'react-native';

export function ClaymorphismNativeCard({ onPress }: { onPress?: () => void }) {
  const compact = useWindowDimensions().width < 600;

  return (
    <View style={styles.page}>
      <View style={[styles.card, compact && styles.compact]}>
        <Text style={styles.title}>Welcome back</Text>
        <Text style={styles.body}>Use soft volume for the object, but keep content and focus states crisp.</Text>
        <Pressable
          accessibilityRole="button"
          accessibilityState={{ disabled: !onPress }}
          disabled={!onPress}
          onPress={onPress}
          style={({ pressed }) => [styles.button, pressed && styles.pressed, !onPress && styles.disabled]}
        >
          <Text style={styles.label}>Continue learning</Text>
        </Pressable>
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  page: { padding: 20, backgroundColor: '#f4f1fb' },
  card: {
    maxWidth: 560,
    padding: 24,
    borderRadius: 32,
    backgroundColor: '#cfd4ff',
    shadowColor: '#504196',
    shadowOpacity: 0.28,
    shadowRadius: 14,
    shadowOffset: { width: 0, height: 10 },
    elevation: 7,
  },
  compact: { padding: 16, borderRadius: 24 },
  title: { fontSize: 22, fontWeight: '700', color: '#24233a' },
  body: { marginTop: 8, color: '#58556f' },
  button: {
    marginTop: 18,
    minHeight: 48,
    paddingHorizontal: 18,
    justifyContent: 'center',
    borderRadius: 20,
    borderWidth: 1,
    borderColor: '#554d86',
    backgroundColor: '#ffffff',
    shadowColor: '#504196',
    shadowOpacity: 0.18,
    shadowRadius: 6,
    shadowOffset: { width: 0, height: 3 },
    elevation: 2,
  },
  pressed: { transform: [{ translateY: 1 }], shadowOpacity: 0.05, elevation: 0 },
  disabled: { opacity: 0.55, transform: [] },
  label: { textAlign: 'center', fontWeight: '700', color: '#24233a' },
});

// Verification: native semantics, bounded volume effects, compact layout, pressed/disabled state.
// Fallback: flatten shadow/highlight while retaining opaque surfaces, borders, text, and interaction meaning.
