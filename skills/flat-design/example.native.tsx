import React from 'react';
import { Pressable, StyleSheet, Text, useWindowDimensions, View } from 'react-native';

export function FlatDesignNativeCard({ onPress }: { onPress?: () => void }) {
  const compact = useWindowDimensions().width < 600;
  return (
    <View style={[styles.card, compact && styles.compact]}>
      <Text style={styles.title}>Flat dashboard</Text>
      <Text style={styles.body}>Hierarchy comes from type, spacing, and explicit boundaries.</Text>
      <Pressable accessibilityRole="button" accessibilityState={{ disabled: !onPress }} disabled={!onPress} onPress={onPress} style={({ pressed }) => [styles.button, pressed && styles.pressed]}>
        <Text style={styles.label}>Open</Text>
      </Pressable>
    </View>
  );
}

const styles = StyleSheet.create({
  card: { padding: 20, borderWidth: 1, borderColor: '#6b6b6b', borderRadius: 8, backgroundColor: '#fff' },
  compact: { padding: 16 },
  title: { fontSize: 20, fontWeight: '700' },
  body: { marginTop: 8, color: '#333' },
  button: { marginTop: 16, minHeight: 48, paddingHorizontal: 16, justifyContent: 'center', borderWidth: 1, borderColor: '#222', borderRadius: 6, backgroundColor: '#e9eef5' },
  pressed: { backgroundColor: '#d8e2ef' },
  label: { textAlign: 'center', fontWeight: '700' },
});

// Verification: semantic Pressable, compact layout rule, explicit pressed/disabled behavior.
// Fallback: remove decorative styling; preserve text, border, target size, and state.
